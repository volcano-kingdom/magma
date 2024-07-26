#!/usr/bin/env python
# The C# runtime code this file references is under The MIT License:
#   https://github.com/dotnet/runtime/blob/5535e31/LICENSE.TXT
import io


class Bad7BitIntError(Exception): pass

class BinaryReader:
    def __init__(self, stream, encoding='utf-8'):
        assert isinstance(stream, io.BufferedIOBase)
        assert 'r' in stream.mode
        self._base_stream = stream
        self._encoding = encoding
    @property
    def base_stream(self):
        return self._base_stream

    def read_bytes(self, n:int) -> bytes:
        if len(chunk := self.base_stream.read(n)) != n:
            raise EOFError("Stream has reached end-of-file during read")
        return chunk

    def read_byte(self) -> int:
        return self.read_bytes(1)[0]

    def read_int32(self) -> int:
        return int.from_bytes(self.read_bytes(32//8), 'little', signed=True)

    def read_string(self) -> str:
        length = self.read_7_bit_encoded_int()
        return self.read_bytes(length).decode(self._encoding)

    def read_7_bit_encoded_int(self) -> int:
        # TODO use a sized type to handle negatives properly
        result = 0
        max_bytes = 4
        for shift in range(0, max_bytes * 7, 7):
            current = self.read_byte()
            result |= (current & 0x7F) << shift
            if current <= 0x7F:
                return result
        current = self.read_byte()
        if current > 0b1:
            raise Bad7BitIntError(
                "Too many bytes in what should have been"
                " a 7-bit encoded integer."
            )
        result |= current << (max_bytes * 7);
        return result



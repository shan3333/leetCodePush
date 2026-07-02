class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        read = 0
        write = 0
        while read < len(chars):
            cur = chars[read]
            count = 0
            while read < len(chars) and cur == chars[read]:
                read += 1
                count += 1
            
            chars[write] = cur
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        #split path using '/' as separator
        for part in path.split('/'):

            if part == "" or part == ".":
                continue

            # '..' means move to the parent directory
            elif part == "..":
                #go back one directory 
                if stack:
                    stack.pop()

            # otherwise its a valid directory name
            else:
                stack.append(part)

        # joining all valid directories 
        return "/" + "/".join(stack)
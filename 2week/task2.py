class Solution:
    def simplifyPath(self, path: str) -> str:
        while '//' in path:
            path = path.replace('//', '/')
        path = path.strip('/')
        list_input_path = path.split('/')
        list_final_path = list()
        command = ""
        while len(list_input_path) != 0:
            command = list_input_path.pop(0)
            match command:
                case "..":
                    if len(list_final_path) != 0:
                        list_final_path.pop(-1)
                case ".":
                    pass
                case _:
                    list_final_path.append("/" + command)

        if len(list_final_path) == 0:
            list_final_path.append("/")

        return ''.join(list_final_path)
def defangIPaddr(self, address: str) -> str:
        l = address.split('.')
        new_addy = ""
        for i in range(len(l)):
            if i == len(l) - 1:
                new_addy += l[i]
            else:
                new_addy += l[i]
                new_addy += "[.]"
        return new_addy
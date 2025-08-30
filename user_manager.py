import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    user_manager = UserManager()
    try:
        for i in range(1000):
            user_manager.add_user(i, f"Usuario {i}")
        print("RNF1 - Se agregaron 1000 usuarios sin errores")

        import time
        start = time.time()
        user_manager.find_user(500)
        end = time.time()
        print("Tiempo de búsqueda usuario 500:", end - start, "s")

    except Exception as e:
        print("Error durante la prueba de rendimiento:", e)

print("end")
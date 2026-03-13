class User:
    def __init__(self, first_name, last_name, age, location, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.job = job
        self.login_attempts = 0 
        
    def describe_user(self):
        print(f"Ringkasan Profil: {self.first_name} {self.last_name}")
        print(f"Pekerjaan: {self.job} | Lokasi: {self.location}")
        
    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
from restaurant import Restaurant
from user import User

print("=== PENGUJIAN KELAS RESTAURANT ===")
my_resto = Restaurant("Warung Padang Sederhana", "Padang")
my_resto.describe_restaurant()

my_resto.increment_number_served(100)
print(f"Total pelanggan dilayani: {my_resto.number_served} orang")

print("\n=== PENGUJIAN KELAS USER ===")
admin_user = User("M.Rafli", "Aswiansyah", 19, "Tembilahan", "Arkeolog")
admin_user.greet_user()

admin_user.increment_login_attempts()
admin_user.increment_login_attempts()
print(f"Percobaan login {admin_user.first_name} {admin_user.last_name}: {admin_user.login_attempts} kali.")

admin_user.reset_login_attempts()
print(f"Percobaan login setelah reset: {admin_user.login_attempts} kali.")
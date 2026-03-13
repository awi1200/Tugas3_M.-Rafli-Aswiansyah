class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 
        
    def describe_restaurant(self):
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"Restoran {self.restaurant_name} sekarang sudah buka!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_served):
        # Memastikan angka yang dimasukkan tidak negatif
        if additional_served >= 0:
            self.number_served += additional_served
        else:
            print("Pesan Error: Jumlah pelanggan tidak bisa negatif!")
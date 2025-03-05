import sqlite3


def perform():
    while True:  # This will create a loop to ask if the user wants to continue after each task
        data_1 = input("Enter the task you want to perform:\n"
                       "1 for creating table\n"
                       "2 for inserting data\n"
                       "3 for updating data\n"
                       "4 for deleting data\n"
                       "5 for selecting data\n"
                       "Type 'exit' to quit\n")

        if data_1.lower() == 'exit':
            print("Exiting the program.")
            break

        con = sqlite3.connect('model1.db')
        print("Connection opened")

        # Enable foreign key constraints in SQLite (they are off by default)
        con.execute("PRAGMA foreign_keys = ON;")

        try:
            if data_1 == "1":
                data_2 = input("Enter the task you want to perform:\n"
                               "1 for creating user table\n"
                               "2 for creating home table\n"
                               "3 for creating floor table\n"
                               "4 for creating room table\n")

                if data_2 == "1":
                    task = """
                        CREATE TABLE IF NOT EXISTS user (
                            _id INTEGER PRIMARY KEY AUTOINCREMENT,  
                            name TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            user_name TEXT NOT NULL UNIQUE,  
                            password TEXT NOT NULL,
                            country TEXT NOT NULL
                        );
                    """
                elif data_2 == "2":
                    task = """
                        CREATE TABLE IF NOT EXISTS home_data (
                            _hid INTEGER PRIMARY KEY AUTOINCREMENT, 
                            _u_name TEXT NOT NULL,
                            home_name TEXT NOT NULL,
                            FOREIGN KEY(_u_name) REFERENCES user(user_name)
                        );
                    """
                elif data_2 == "3":
                    task = """
                        CREATE TABLE IF NOT EXISTS floor_data (
                            _u_name TEXT NOT NULL,
                            _h_id INTEGER NOT NULL,  
                            floor_name TEXT NOT NULL,
                            floor_level INTEGER NOT NULL,
                            PRIMARY KEY (_u_name, _h_id, floor_name),
                            FOREIGN KEY(_u_name) REFERENCES user(user_name),
                            FOREIGN KEY(_h_id) REFERENCES home_data(_hid)
                        );
                    """
                elif data_2 == "4":
                    task = """
                        CREATE TABLE IF NOT EXISTS room_data (
                            _u_name TEXT NOT NULL,
                            _h_id INTEGER NOT NULL, 
                            _f_name TEXT NOT NULL,  
                            room_name TEXT NOT NULL,
                            PRIMARY KEY (_u_name, _h_id, _f_name, room_name),  
                            FOREIGN KEY(_u_name, _h_id, _f_name) REFERENCES floor_data(_u_name, _h_id, floor_name),
                            FOREIGN KEY(_u_name) REFERENCES user(user_name),
                            FOREIGN KEY(_h_id) REFERENCES home_data(_hid)  
                        );
                    """
                else:
                    print("Invalid choice for table creation.")
                    continue

            elif data_1 == "2":
                data_2 = input("Enter the task you want to perform:\n"
                               "1 for inserting into user table\n"
                               "2 for inserting into home table\n"
                               "3 for inserting into floor table\n"
                               "4 for inserting into room table\n")

                if data_2 == "1":
                    name = input("Enter user name: ")
                    email = input("Enter user email: ")
                    user_name = input("Enter user username: ")
                    password = input("Enter user password: ")
                    country = input("Enter user country: ")
                    task = f"""
                        INSERT INTO user (name, email, user_name, password, country)
                        VALUES ('{name}', '{email}', '{user_name}', '{password}', '{country}');
                    """
                elif data_2 == "2":
                    user_name = input("Enter the user username for home: ")
                    home_name = input("Enter the home name: ")
                    task = f"""
                        INSERT INTO home_data (_u_name, home_name)
                        VALUES ('{user_name}', '{home_name}');
                    """
                elif data_2 == "3":
                    user_name = input("Enter the user username for floor: ")
                    home_id = int(input("Enter the home ID: "))
                    floor_name = input("Enter the floor name: ")
                    floor_level = int(input("Enter the floor level: "))
                    task = f"""
                        INSERT INTO floor_data (_u_name, _h_id, floor_name, floor_level)
                        VALUES ('{user_name}', {home_id}, '{floor_name}', {floor_level});
                    """
                elif data_2 == "4":
                    user_name = input("Enter the user username for room: ")
                    home_id = int(input("Enter the home ID: "))
                    floor_name = input("Enter the floor name: ")
                    room_name = input("Enter the room name: ")
                    task = f"""
                        INSERT INTO room_data (_u_name, _h_id, _f_name, room_name)
                        VALUES ('{user_name}', {home_id}, '{floor_name}', '{room_name}');
                    """
                else:
                    print("Invalid choice for inserting data.")
                    continue

            elif data_1 == "3":
                data_2 = input("Enter the task you want to perform:\n"
                               "1 for updating user table\n"
                               "2 for updating home table\n"
                               "3 for updating floor table\n"
                               "4 for updating room table\n")

                if data_2 == "1":
                    user_name = input("Enter the user_name of the user to update: ")
                    new_name = input("Enter the new name: ")
                    task = f"""
                        UPDATE user
                        SET name = '{new_name}'
                        WHERE user_name = '{user_name}';
                    """
                elif data_2 == "2":
                    home_name = input("Enter the home name to update: ")
                    new_home_name = input("Enter the new home name: ")
                    task = f"""
                        UPDATE home_data
                        SET home_name = '{new_home_name}'
                        WHERE home_name = '{home_name}';
                    """
                elif data_2 == "3":
                    floor_name = input("Enter the floor name to update: ")
                    new_floor_level = int(input("Enter the new floor level: "))
                    task = f"""
                        UPDATE floor_data
                        SET floor_level = {new_floor_level}
                        WHERE floor_name = '{floor_name}';
                    """
                elif data_2 == "4":
                    room_name = input("Enter the room name to update: ")
                    new_room_name = input("Enter the new room name: ")
                    task = f"""
                        UPDATE room_data
                        SET room_name = '{new_room_name}'
                        WHERE room_name = '{room_name}';
                    """
                else:
                    print("Invalid choice for updating data.")
                    continue

            elif data_1 == "4":
                data_2 = input("Enter the task you want to perform:\n"
                               "1 for deleting from user table\n"
                               "2 for deleting from home table\n"
                               "3 for deleting from floor table\n"
                               "4 for deleting from room table\n")

                if data_2 == "1":
                    user_name = input("Enter the user_name of the user to delete: ")
                    task = f"""
                        DELETE FROM user
                        WHERE user_name = '{user_name}';
                    """
                elif data_2 == "2":
                    home_name = input("Enter the home name to delete: ")
                    task = f"""
                        DELETE FROM home_data
                        WHERE home_name = '{home_name}';
                    """
                elif data_2 == "3":
                    floor_name = input("Enter the floor name to delete: ")
                    task = f"""
                        DELETE FROM floor_data
                        WHERE floor_name = '{floor_name}';
                    """
                elif data_2 == "4":
                    room_name = input("Enter the room name to delete: ")
                    task = f"""
                        DELETE FROM room_data
                        WHERE room_name = '{room_name}';
                    """
                else:
                    print("Invalid choice for deleting data.")
                    continue

            elif data_1 == "5":
                data_2 = input("Enter the task you want to perform:\n"
                               "1 for selecting from user table\n"
                               "2 for selecting from home table\n"
                               "3 for selecting from floor table\n"
                               "4 for selecting from room table\n")

                if data_2 == "1":
                    task = "SELECT * FROM user;"
                elif data_2 == "2":
                    task = "SELECT * FROM home_data;"
                elif data_2 == "3":
                    task = "SELECT * FROM floor_data;"
                elif data_2 == "4":
                    task = "SELECT * FROM room_data;"
                else:
                    print("Invalid choice for selecting data.")
                    continue

                cursor = con.execute(task)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                continue

            else:
                print("Invalid choice.")
                continue

            # Execute the SQL task
            con.execute(task)

            # Commit changes to the database
            con.commit()
            print("Task has been performed successfully.")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

        finally:
            con.close()
            print("Connection closed.")

        # Ask the user if they want to continue or terminate
        user_input = input("Do you want to perform another task? (yes/no): ").strip().lower()
        if user_input != 'yes':
            print("Exiting the program.")
            break  # Exit the loop and terminate the program


# Run the perform function
perform()

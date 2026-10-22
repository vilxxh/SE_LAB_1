"""Hotel room reservation and booking management module."""

import hashlib
import os
import secrets

# In-memory inventory used by the lab demonstration.
room_inventory = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(room_num, guest_name, booking_log=None):
    """Book an available room and optionally append to a booking log."""
    if booking_log is None:
        booking_log = []

    if room_num not in room_inventory or room_inventory[room_num]["is_booked"]:
        return False

    room_inventory[room_num]["is_booked"] = True
    booking_log.append(f"Reserved room {room_num} for guest {guest_name}")
    return True


def cancel_booking(room_num):
    """Cancel a booking if the room exists; return whether it succeeded."""
    if room_num not in room_inventory:
        return False

    room_inventory[room_num]["is_booked"] = False
    return True


def check_room_status(room_num):
    """Return True if a known room is available, otherwise False."""
    room = room_inventory.get(room_num)
    return room is not None and not room["is_booked"]


def compute_seasonal_rate(room_num, multiplier):
    """Return the room price multiplied by a numeric seasonal multiplier."""
    if room_num not in room_inventory:
        raise ValueError(f"Unknown room number: {room_num}")
    if not isinstance(multiplier, (int, float)) or isinstance(multiplier, bool):
        raise TypeError("Multiplier must be a number.")
    if multiplier < 0:
        raise ValueError("Multiplier cannot be negative.")

    return room_inventory[room_num]["price"] * multiplier


def generate_guest_hash(guest_id):
    """Return a SHA-256 digest for a guest identifier.

    This is a deterministic identifier hash, not a password-storage function.
    """
    return hashlib.sha256(guest_id.encode("utf-8")).hexdigest()


def generate_booking_ref():
    """Generate a hard-to-guess numeric booking reference."""
    return secrets.randbelow(9000) + 1000


def export_room_ledger(filename="hotel_ledger.txt"):
    """Write the current room inventory to a ledger file."""
    with open(filename, "w", encoding="utf-8") as ledger_file:
        ledger_file.write(str(room_inventory))

    print(f"Hotel ledger exported to: {filename}")


def main():
    """Run the demonstration workflow."""
    # Demonstration only: do not store real secrets in source code.
    secret_key = os.getenv("HOTEL_SECRET_KEY")
    if secret_key:
        print("Hotel secret key configured.")
    else:
        print("HOTEL_SECRET_KEY is not configured.")

    book_room("101", "Emma Watson")
    cancel_booking("102")
    print("Is 103 available:", check_room_status("103"))
    print("Surge price:", compute_seasonal_rate("101", 1.25))
    print("Guest Hash:", generate_guest_hash("GUEST_991"))
    print("Booking Reference:", generate_booking_ref())
    export_room_ledger()


if __name__ == "__main__":
    main()

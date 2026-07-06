"""
Universal Observatory Operating System
CLI App v0.1

Purpose:
Simple command interface for testing the Registry Engine.
"""

from uos.kernel.registry import (
    create_object,
    list_objects,
    search_objects,
    add_boundary,
    add_unknown,
    export_registry,
)


def print_object(obj):
    print("-" * 60)
    print(f"ID:       {obj.get('id')}")
    print(f"Name:     {obj.get('name')}")
    print(f"Category: {obj.get('category')}")
    print(f"Domain:   {obj.get('domain')}")
    print(f"Scale:    {obj.get('scale')}")
    print(f"Status:   {obj.get('status')}")
    print(f"Tags:     {', '.join(obj.get('tags', []))}")
    print(f"Notes:    {obj.get('notes', '')}")


def main():
    while True:
        print("\nUNIVERSAL OBSERVATORY OS")
        print("1. List objects")
        print("2. Add object")
        print("3. Search objects")
        print("4. Add boundary")
        print("5. Add unknown")
        print("6. Export registry")
        print("0. Exit")

        choice = input("\nSelect: ").strip()

        if choice == "1":
            objects = list_objects()
            print(f"\nObjects: {len(objects)}")
            for obj in objects:
                print_object(obj)

        elif choice == "2":
            name = input("Name: ").strip()
            category = input("Category: ").strip()
            description = input("Description: ").strip()
            domain = input("Domain: ").strip()
            scale = input("Scale: ").strip()
            status = input("Status: ").strip() or "unknown"
            tags_raw = input("Tags comma-separated: ").strip()
            tags = [t.strip() for t in tags_raw.split(",") if t.strip()]

            obj = create_object(
                name=name,
                category=category,
                description=description,
                domain=domain,
                scale=scale,
                status=status,
                tags=tags,
            )
            print("\nCreated:")
            print_object(obj)

        elif choice == "3":
            query = input("Search query: ").strip()
            results = search_objects(query)
            print(f"\nResults: {len(results)}")
            for obj in results:
                print_object(obj)

        elif choice == "4":
            object_id = input("Object ID: ").strip()
            boundary = input("Boundary: ").strip()
            updated = add_boundary(object_id, boundary)
            print("Boundary added." if updated else "Object not found.")

        elif choice == "5":
            object_id = input("Object ID: ").strip()
            unknown = input("Unknown: ").strip()
            updated = add_unknown(object_id, unknown)
            print("Unknown added." if updated else "Object not found.")

        elif choice == "6":
            path = export_registry()
            print(f"Exported registry to: {path}")

        elif choice == "0":
            print("Exiting.")
            break

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
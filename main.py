from agent import get_answer

cache = {}

def main():
    print("⚡ Fast AI SQL Agent Ready! (type 'exit' to quit)\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        if query in cache:
            print("\n⚡ Cached:", cache[query], "\n")
            continue

        try:
            sql, result = get_answer(query)

            print("\nGenerated SQL:")
            print(sql)

            print("\nResult:")
            print(result, "\n")

            cache[query] = result

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()

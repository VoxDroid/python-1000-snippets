
            # sample1.py
            # Parse an INI file and print values.

            import configparser
            import os
            import tempfile

            def main() -> None:
                config = configparser.ConfigParser()
                with tempfile.TemporaryDirectory(prefix="ini_") as tmpdir:
                    ini_path = os.path.join(tmpdir, "settings.ini")
                    with open(ini_path, "w", encoding="utf-8") as f:
                        f.write("""[server]
")
                        f.write("host = localhost
")
                        f.write("port = 8000
")
                        f.write("[user]
")
                        f.write("name = alice
")
                        f.write("email = alice@example.com
")

                    config.read(ini_path)
                    print("Server host:", config["server"]["host"])
                    print("Server port:", config.getint("server", "port"))
                    print("User name:", config["user"]["name"])

            if __name__ == "__main__":
                main()

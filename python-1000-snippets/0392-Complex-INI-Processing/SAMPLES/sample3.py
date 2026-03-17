
            # sample3.py
            # Demonstrates interpolation across sections using ExtendedInterpolation.

            import configparser
            import os
            import tempfile

            def main() -> None:
                config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

                with tempfile.TemporaryDirectory(prefix="ini_") as tmpdir:
                    ini_path = os.path.join(tmpdir, "interp.ini")
                    with open(ini_path, "w", encoding="utf-8") as f:
                        f.write("""[paths]
")
                        f.write("base = /usr/local
")
                        f.write("bin = ${paths:base}/bin
")
                        f.write("[app]
")
                        f.write("exec = ${paths:bin}/myapp
")

                    config.read(ini_path)
                    print("Base path:", config["paths"]["base"])
                    print("Bin path:", config["paths"]["bin"])
                    print("Exec path:", config["app"]["exec"])

            if __name__ == "__main__":
                main()

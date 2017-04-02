import cx_Freeze

executables = [cx_Freeze.Executable("pacman.pyw")]

cx_Freeze.setup(
    name = "Pacman",
    options = {"build_exe":{"packages":["pygame"],"include_files":["res"],}},
    description = "Pacman Python",
    executables = executables

    )

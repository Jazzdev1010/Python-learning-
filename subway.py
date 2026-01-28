def create_subway(size, bread = "multi-grain", *args, **kwargs):
    print(f"Your subway size is:{size}")
    print(f"You have ordered:{args[0]} subway")
    print(f"Your subway bread is:{bread}")
    print(f"Your subway veges are:{kwargs.get("veges")}")
    print(f"Your subway sauces are:{kwargs.get("sauce")}")


ajit = create_subway(30, "honey-bread", 2, veges=["olive", "cucumber", "chilli"], sauce=["honey-mustard", "bbq", "hot-chilli"])
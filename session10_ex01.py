cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]

while True :
    print("""
-------------------------------------
--- SHOPEE CART MANAGEMENT SYSTEM --- 
-------------------------------------
1. Xem chi tiết giỏ hàng và tính tổng tiền 
2. Thêm sản phẩm mới / cộng dồn số lượng
3. Cập nhật số lượng của 1 sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
""")    
    choice = input("Mời bạn nhập chức năng (1-5): ").strip()

    if choice == "1" :
        if cart_items == [] :
            print("Giỏ hàng trống!") 
        else :
            total_cart_amount = 0
            total_cart_price = 0
            
            print("--- CHI TIẾT GIỎ HÀNG ---")    
            print("STT | Mã SP  | Tên sản phẩm         | SL  | Đơn giá     | Thành tiền")
            
            for i, cart in enumerate(cart_items, start=1) :
                cart_id = cart[0]
                cart_name = cart[1]
                cart_amount = cart[2]
                cart_price = cart[3]
                final_cart_price = (cart_amount * cart_price)

                print(f"{i:<3} | {cart_id:<6} | {cart_name:<20} | {cart_amount:<3} | {cart_price:<11}đ | {final_cart_price}đ")
            
                total_cart_amount += cart_amount
                total_cart_price += final_cart_price

            print(f"--> Tổng số lượng sản phẩm trong giỏ: {total_cart_amount}")
            print(f"--> Tổng tiền thanh toán: {total_cart_price}đ")

    elif choice == '2' :
        add_cart_items_id = input("Nhập mã sản phẩm: ").strip()
        add_cart_items_name = input("Nhập tên sản phẩm: ").strip()
        
        while True:
            add_cart_items_amount = int(input("Nhập số lượng sản phẩm: ").strip())
            if add_cart_items_amount <= 0:
                print("Số lượng phải lớn hơn 0!")
                continue
            break

        while True:
            add_cart_items_price = int(input("Nhập giá sản phẩm: ").strip())
            if add_cart_items_price <= 0:
                print("Giá phải lớn hơn 0!")
                continue
            break

        for cart in cart_items :
            if cart[0] == add_cart_items_id :
                cart[2] += add_cart_items_amount
                print("Mã sản phẩm đã tồn tại! Tự động cộng dồn số lượng.")
                break
        else :
            new_cart = [add_cart_items_id, add_cart_items_name, add_cart_items_amount ,add_cart_items_price]
            cart_items.append(new_cart)
            print("Thêm mới thành công!")

    elif choice == '3':
        if cart_items == []:
            print("Giỏ hàng trống!")
            continue
            
        update_id = input("Nhập mã sản phẩm cần sửa số lượng: ").strip()
        for cart in cart_items:
            if cart[0] == update_id:
                while True:
                    update_amount = int(input(f"Nhập số lượng mới cho sản phẩm {update_id}: ").strip())
                    if update_amount <= 0:
                        print("Số lượng phải lớn hơn 0!")
                        continue
                    break
                    
                cart[2] = update_amount
                print("Cập nhật số lượng mới thành công!")
                break
        else:
            print("Mã sản phẩm không tồn tại!")

    elif choice == '4':
        if cart_items == []:
            print("Giỏ hàng trống!")
            continue
            
        delete_cart_items_id = input("Nhập mã sản phẩm để xóa: ").strip()
        for cart in cart_items:
            if delete_cart_items_id == cart[0]:
                cart_items.remove(cart)
                print("Xóa thành công!")
                break
        else :
            print("Mã sản phẩm không tồn tại!")

    elif choice == "5":
        print("Thoát chương trình!")
        break
        
    else :
        print("Vui lòng nhập lại (1-5)!")
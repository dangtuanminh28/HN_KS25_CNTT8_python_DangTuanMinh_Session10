sound_track = ["Legend", "Quite", "Peace", "Mix", "Sad"]

while True :
    print("""
--- MENU QUẢN LÝ DANH SÁCH PHÁT --- 
1. Thêm bài hát vào danh sách phát
2. Xem danh sách phát
3. Xóa bài hát khỏi danh sách phát
4. Sắp xếp và trích xuất khỏi danh sách
5. Thoát chương trình
""")
    choice = input("Mời bạn nhập chức năng (1-5): ").strip()

    if choice == "1" :
        while True :
            print("""
--- THÊM BÀI HÁT ---
1. Thêm vào cuối danh sách
2. Chèn vào vị trí cụ thể
""")
            choice_sub = input("Nhập lựa chọn (1-2): ").strip()
            
            if choice_sub == "1":
                while True:
                    add_sound_track = input("Nhập tên bài hát: ").strip()
                    if add_sound_track == "":
                        print("Tên bài hát không được để trống!")
                        continue
                    break
                    
                sound_track.append(add_sound_track)
                print(f"-> Thêm thành công bài hát: {add_sound_track}")
                print(f"Số lượng bài hát hiện tại: {len(sound_track)}")
                break
                
            elif choice_sub == "2":
                while True:
                    add_sound_track = input("Nhập tên bài hát: ").strip()
                    if add_sound_track == "":
                        print("Tên bài hát không được để trống!")
                        continue
                    break
                    
                while True:
                    pos_str = input(f"Nhập số thứ tự muốn chèn (1 - {len(sound_track) + 1}): ").strip()
                    
                    valid_positions = []
                    for num in range(1, len(sound_track) + 2):
                        valid_positions.append(str(num))
                        
                    if pos_str not in valid_positions:
                        print(f"Vị trí không hợp lệ!")
                        continue
                        
                    position = int(pos_str)
                    sound_track.insert(position - 1, add_sound_track)
                    print(f"-> Chèn thành công bài hát '{add_sound_track}' vào vị trí {position}!")
                    print(f"Số lượng bài hát hiện tại: {len(sound_track)}")
                    break
                break
            else :
                print("Vui lòng nhập lại (1-2)!")

    elif choice == '2' :
        if sound_track == [] :
            print("Danh sách phát hiện đang trống!") 
        else :
            print("---DANH SÁCH PHÁT ---")    
            for i, sound in enumerate(sound_track, start=1) :
                print(f"{i}. {sound}")
            print(f"Tổng số bài hát: {len(sound_track)}")

    elif choice == '3':
        if sound_track == [] :
            print("Danh sách phát hiện đang trống!")
            continue
            
        while True :
            print("""
--- XÓA BÀI HÁT ---
1. Xóa theo tên bài hát 
2. Xóa theo số thứ tự
""")
            choice_sub = input("Nhập lựa chọn (1-2): ").strip()
               
            if choice_sub == "1":
                del_name = input("Nhập tên bài hát muốn xóa: ").strip()
                if del_name in sound_track:
                    sound_track.remove(del_name)
                    print(f"Đã xóa bài hát [{del_name}] khỏi danh sách")
                else:
                    print("Không tìm thấy bài hát trong danh sách phát")
                break
                
            elif choice_sub == "2":
                while True:
                    del_idx_str = input(f"Nhập số thứ tự bài hát muốn xóa: ").strip()
                    
                    valid_indexes = []
                    for num in range(1, len(sound_track) + 1):
                        valid_indexes.append(str(num))
                        
                    if del_idx_str not in valid_indexes:
                        print(f"Vị trí không hợp lệ!")
                        continue
                        
                    del_index = int(del_idx_str)
                    removed_song = sound_track.pop(del_index - 1)
                    print(f"Đã xóa bài hát [{removed_song}] khỏi danh sách")
                    break
                break
            else :
                print("Vui lòng nhập lại (1-2)!")

    elif choice == '4':
        if sound_track == [] :
            print("Danh sách phát hiện đang trống!")
            continue
            
        while True:
            print("""
--- SẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH ---
1. Sắp xếp danh sách phát theo bảng chữ cái A-Z
2. Hiển thị 3 bài hát đầu tiên
""")
            choice_sub = input("Nhập lựa chọn (1-2): ").strip()
                    
            if choice_sub == "1":
                sound_track.sort()
                print("Đã sắp xếp thành công!")
                break
            elif choice_sub == "2":
                print("--- 3 BÀI HÁT ĐẦU TIÊN ---")
                top_3 = sound_track[:3]
                for i, sound in enumerate(top_3, start=1):
                    print(f"{i}. {sound}")
                break
            else :
                print("Vui lòng nhập lại (1-2)!")

    elif choice == "5":
        print("Thoát chương trình!")
        break
        
    else :
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên")
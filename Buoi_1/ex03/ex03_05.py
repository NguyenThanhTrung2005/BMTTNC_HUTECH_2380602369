def dem_so_lan_xuat_hien(lst):
    count_dick = {}
    for item in lst:
        if item in count_dick:
            count_dick[item] += 1
        else:
            count_dick[item] = 1
    return count_dick
    
input_string = input("Nhap danh sach cac tu, cach nhau bang dau cach: ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac phan tu:", so_lan_xuat_hien)
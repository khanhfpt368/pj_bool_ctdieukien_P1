# Thu Vien
from functools import cmp_to_key # thu bien sap xep theo do uu tien



# Cac phuong thuc trong Boolean
def KT_sochan(a):  # BT01 ham ktra chan
    if (a > 0) and (a % 2 ==0 ):
        return '---> Day la so chan'
    else:
        return '---> Day la so le'

def KT_kytuchuoi(chuoi): # BT02 ham ktra chuoi in hoa, chuoi thuong hoac ca 2
    if chuoi.isupper():
        return '---> Day la chuoi in hoa'
    elif chuoi.islower():
        return '---> Day la chuoi thuong'
    elif chuoi.title():
        return '---> Day la chuoi co cac ky tu dau in hoa'
    else:
        return '---> Day la chuoi co cac ky tu in hoa va thuong Random'

def KT_chuoicon(st, st_search): # BT03: Tim chuoi con tu 1 chuoi nhap vao truoc do
    if st_search in st:
        return '---> Da tim thay chuoi con can tim, tai vi tri: '+ str(st.find(st_search))
    else:
        return 'Ko tim thay chuoi con can tim'

def Tim_solonnhat(num1, num2, num3): # BT04: Tim so lon nhat
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3

def Phanloai_tamgiac(canh_a, canh_b, canh_c): # BT05:Phan loai tam giac
    if canh_a == canh_b == canh_c:
        tri_type = '---> Day la Tam Giac Deu'
        print( ' ++ Tam giac co 3 canh bang nhau. Do dai cac canh A, B, C: ',canh_a, canh_b, canh_c)
    elif (canh_a == canh_b != canh_c) or (canh_a == canh_c != canh_b) or (canh_b == canh_c != canh_a):
        tri_type = '---> Day la Tam Giac Can'
        print('++ Tam giac co 2 canh bang nhau va 1 canh khac nhau. Do dai cua cac canh A, B, C: ',canh_a,canh_b,canh_c)
    else:
        tri_type = '---> Day la Tam Giac Thuong'
        print( '++ Tam giac co 3 canh khac nhau.Do dai cua cac canh A, B, C: ',canh_a,canh_b,canh_c)
    print(tri_type)

def KT_daysofmonth(month): # BT06:Tim so ngay trong thang, nhap vao
    if month == 'April' or month == 'Thang 4' or month == 'June' or month == 'Thang 6' or month == 'September' or month == 'Thang 9' or month == 'November'or month == 'Thang 11':
        days = '30 days/ ngay'
    elif month == 'February'or month == 'Thang 2':
        days = '28 or 29 days/ ngay'
    else:
        days = '31 days/ ngay'
    return days

def KT_nguyenphuam(don_am): # BT07:KT nguyen am hay phu am, nhap vao
    if(don_am == 'a' or don_am == 'e' or don_am == 'i' or don_am == 'o' or don_am == 'u'):
        return '---> Ki Tu Nay La Nguyen Am'
    elif(don_am == 'y'):
        return '---> Ki Tu Nay Co The La Nguyen Am Hoac Phu Am'
    else:
        return '---> Ki Tu Nay La Phu Am'

# Tạo DS cac phuong thuc thuc thi theo thu tu tu tren xuong trong DS co san [tham khao them]
#List_method = [KT_sochan, KT_kytuchuoi, KT_chuoicon, Tim_solonnhat, Phanloai_tamgiac]
#for method in List_method:
 #   method()

# Nhap cac bien dau vao
## BT01:
a = int(input('Nhap so a = '))
## BT02:
chuoi = input('Nhap chuoi can kiem tra: ')
## BT03:
st = input('Nhap chuoi me can kiem tra: ')
st_search = input('Nhap chuoi con can tim: ')
## BT04:
num1 = float(input('Nhap so thu nhat = '))
num2 = float(input('Nhap so thu 2 = '))
num3 = float(input('Nhap so thu 3 = '))
## BT05:
canh_a = float(input('Nhap canh A = '))
canh_b = float(input('Nhap canh B = '))
canh_c = float(input('Nhap canh C = '))
## BT06:
month = input('Nhap thang can tim: ')
## BT07:
don_am = input('Nhap don am can kiem tra: ')

# Goi phuong thuc sdung
## BT01:
KT_chan = KT_sochan(a)
## BT02:
Check_string = KT_kytuchuoi(chuoi)
## BT03:
Check_chuoicon = KT_chuoicon(st, st_search)
## BT04:
Max_3so = Tim_solonnhat(num1, num2, num3)
# BT05:
# BT06:
Songay_cuathang = KT_daysofmonth(month)
# BT07:
Check_am = KT_nguyenphuam(don_am)
# In ra man hinh
print(KT_chan)
print(Check_string)
print(Check_chuoicon)
print('---> So lon nhat trong 3 so :', Max_3so)
## BT05:
Phanloai_tamgiac(canh_a, canh_b, canh_c)
print('--> Month/ Thang: ', month,' Have/ Co: ', Songay_cuathang)
print(Check_am)

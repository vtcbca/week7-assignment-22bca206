### Create CSV file for product selling for 6 Months ( Prod_No | Prod_Name | Jan | Feb | Mar | Apr | May | Jun) for 5 products.

import csv
heading=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']

def input_data_from_user():
    list1=[]
    for i in range(int(input("How Many Records You Want To Insert into File:"))):
        pno=int(input("Enter Product Number : "))
        pname=input('Enter Product Name : ')
        jan=int(input("How Many Product Sold In January ?: "))
        feb=int(input("How Many Product Sold In Fabruary ?: "))
        mar=int(input("How Many Product Sold In March ?: "))
        apr=int(input("How Many Product Sold In April ?: "))
        may=int(input("How Many Product Sold In may ?: "))
        june=int(input("How Many Product Sold In June ?: "))
        l=[pno,pname,jan,feb,mar,apr,may,june]
        list1.append(l) 
    return list1

with open(r'D:\Product_Details.csv','w',newline='') as file:
    obj=csv.writer(file)
    obj.writerow(heading)
    obj.writerows(input_data_from_user())
       

# 2. Create dataframe.

import pandas as pn

df=pn.read_csv(r'D:\product_details.csv')
df

### 3. Change Column Name Product No, Product Name, January, February, March, April, May, June.

dic={
        'Prod_No':'Product NO',
        'Prod_Name':'Product Name',
        'Jan':'January',
        'Feb':'February',
        'Mar':'March',
        'Apr':'April',
        'May':'May',
        'Jun':'June'
}
df.rename(columns=dic,inplace=True)
df

### 4. Add column "Total Sell" to count total of all month and "Average Sell"

total=df['January']+df['February']+df['March']+df['April']+df['May']+df['June']
df['Total Sell']=total
aveg=df['Total Sell']/6
df['Average Sell']=aveg
df

### 5. Add 2 row at the end.

item1={
        'Product NO':10,
        'Product Name':'Godiva chocolates',
        'January':12000,
        'February':23000,
        'March':15000,
        'April':19000,
        'May':11000,
        'June':14500,
        'Total Sell':94500,
        'Average Sell':15750
}
data=pn.DataFrame(item1,index=[len(df)+1])
item2={
        'Product NO':11,
        'Product Name':'Pacari Chocolates',
        'January':2300,
        'February':29000,
        'March':15000,
        'April':30000,
        'May':11000,
        'June':14500,
        'Total Sell':101800,
        'Average Sell':16966.6666667
}
data1=pn.DataFrame(item2,index=[len(df)+2])
df=pn.concat([df,data,data1])
df

### 6. Add 2 row after 3rd row.

df.loc[2.5]=[12,'Fabelle Exquisite chocolates',14500,15000,11000,16000,21000,19000,96500,16083.333333]
df.sort_index().reset_index(drop=True)
df.loc[2.5]=[13,'Nestle Chocolates',16000,17000,21000,17000,12500,23000,106500,17750]
df.sort_index().reset_index(drop=True)
df

### 7. Print first 5 row.

df.head()

### 8. Print Last 5 row.

df.tail()

### 9. Print row 6 to 10.

df.iloc[6:11]

### 10. Print only product name.

df['Product Name']

### 11. Print sell of January month with product id and product name.

df[['Product NO','Product Name','January']]

### 12. Print only those product id , product name where january sell is > 5000 and February sell is >8000

df[['Product NO','Product Name']][(df['January']>5000)&(df['February']>8000)]


### 13. Print record in sorting order of Product name.

df.sort_values(by='Product Name')

### 14. Display only odd index number column record.

df.iloc[0:len(df):3]

### 15. Display alternate row.

df.iloc[0:len(df):2]


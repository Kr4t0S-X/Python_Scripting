import win32com.client

outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
#attachement = "C:\\Users\\SESA571075\\Desktop\\Python_Scripts\\CISO_Letter.pdf"

mail.To = 'charlesfrancois.ghanime@se.com'
mail.Subject = 'This is a test email'
mail.HTMLBody = '<h3>This is HTML Body</h3>'
mail.Body = 'This is the normal Body'
mail.Attachements.Add("C:/Users/SESA571075/Desktop/Python_Scripts/CISO_Letter.pdf")
mail.CC = 'charlesfrancois.ghanime@altran.com'

mail.Send()
from django.shortcuts import render
import pandas as pd
from search_app.models import Users

# Create your views here.
def upload_system(request):
    message = {
        "message": "",
        "color": ""
    }
    if request.method == 'POST':
        if request.FILES:
            try:
                df = None
                sheet = request.FILES.get('sheet')
                if sheet.name.endswith(".csv"):
                    df = pd.read_csv(sheet)
                else:
                    df = pd.read_excel(sheet)

                load_sheet = pd.DataFrame(df)
                for user in range(load_sheet.shape[0]):
                    first_name = load_sheet.iloc[user]["first_name"]
                    last_name = load_sheet.iloc[user]["last_name"]
                    phone = load_sheet.iloc[user]["phone"]
                    email = load_sheet.iloc[user]["email"]
                    Users.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone=phone
                    )
                message['message'] = "File uploaded successfully!."
                message['color'] = "text-success"
            except:
                message['message'] = "The file you uploaded is not valid. Check the file type and also ensure that the values are well described."
                message['color'] = "text-danger"
                

            
    context = {
        'message': message
    }
    return render(request, 'upload_system.html', context)
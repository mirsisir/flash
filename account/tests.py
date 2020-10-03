@login_required(login_url ='singin')
def extrafield(request):
    profile = ExtendedUser.objects.create(user=request.user)
    task_form = ExtendedCreateUserForm

    if request.method == "POST":
        task_form=ExtendedCreateUserForm(data=request.POST)
        if task_form.is_valid():

            task=task_form.save(commit=False)
            task.user= request.user
            task.save()
            return redirect('dashboard')

    context ={
        'task_form':task_form
    }
    return render (request , 'extrafield.html', context )

html update page 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <style>
        .container{
            width: 60%;
            position: absolute;
            left: 15rem;

        }
    </style>
</head>
<body>
    <div class="col-lg-1">
        
    </div>
    <div class="container col-lg-6">

        <br><br><br><br>
        {{update_order.user}}

        
    


        <div class="row">
            <div class="col-md-6">
                <div class="card card-body">
        
                    <form action="" method="POST">
                        {% csrf_token %}
                        {{ form.management_form }}
                        {% for field in form %}
                            {{field.label}} :       
                            {{field}}
                            <hr>
                            <hr>
                        {% endfor %}
                        

                    
                        

                        
                        <input type="submit" name="Submit">
                    </form>
        
                </div>
            </div>
        </div>
    </div>

    
</body>
</html>
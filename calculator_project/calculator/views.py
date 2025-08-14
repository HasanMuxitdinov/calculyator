from django.shortcuts import render


def calculator(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Nolga bo'lish mumkin emas!"
        except ValueError:
            result = "Noto'g'ri kiritish!"

    return render(request, 'calculator/calculator.html', {'result': result})


from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def list_students(request):
    students = Student.objects.values('id', 'name')
    names = [s.name for s in students]
    return JsonResponse({'students': names})

@csrf_exempt
def get_student_details(request, id):
    try:
        student = Student.objects.get(id=id)
        return JsonResponse({
            'student': {
                'id': student.id,
                'name': student.name,
                'roll_number': student.roll_number,
                'email': student.email,
                'phone': student.phone,
                'status': student.status,
                'age': student.age
            }
        })
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)

@csrf_exempt
def create_student(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)
    
    try:
        data = json.loads(request.body)
        student = Student.objects.create(
            name=data.get('name'),
            roll_number=data.get('roll_number'),
            email=data.get('email', ''),
            phone=data.get('phone', ''),
            status=data.get('status', 'active'),
            age=data.get('age', 18)
        )
        return JsonResponse({
            'message': 'Student created successfully',
            'student': {
                'id': student.id,
                'name': student.name,
                'roll_number': student.roll_number
            }
        }, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Answer, Question

# Create your views here.
def home(request):
    return render(request, 'main.html')

#-----기본 메인 화면-----
#소통게시판 : communication_list
def communication_list(request):
    if request.method == 'POST':
        categorys = [0, 1, 2, 3, 4, 5]
        # sorts = ['date', 'likes', 'views', 'answerd', 'notAnswerd']
        sort = 'date'

        index=0
        for category in categorys:
            if index==0:
                questions = Question.objects.filter(category=category)
            else:
                index+=1
                question = Question.objects.filter(category=category)
                questions.union(question)

        if sort == 'date':
            communication_list = questions.order_by('-date')
        elif sort == 'likes':
            communication_list = questions.order_by('-recommend')
        elif sort == 'views':
            communication_list = questions.order_by('-views')
        elif sort == 'answerd':
            communication_list = questions.filter(answerd=True).order_by('-date')
        else:
            communication_list = questions.filter(answerd=False).order_by('-date')
    else:
        communication_list = Question.objects.all().order_by('-date')

    noQuestion = Question.objects.filter(answerd=False).exclude(autor=request.user).order_by("?")[:2]
    myQuestion = Question.objects.filter(autor=request.user).order_by("?")[:2]
    context = {
        'communication_list': communication_list,
        'noQuestion': noQuestion,
        'myQuestion': myQuestion,

    }
    return render(request, 'communicationApp/communication.html', context)

#소통게시판 메인_질문하나 클릭하면 나오는 화면 : communication_detail
def communication_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    category = question.category
    question.views += 1
    
    sameCategory = Question.objects.filter(category=category).exclude(pk=question_id).order_by("?")[:5]

    context = {
        'question': question,
        'sameCategory': sameCategory,
    }
    return render(request, 'communicationAPP/question-detail.html', context)

#답변하기 : answer_list
def answer_list(request):
    if request.method == 'POST':
        categorys = [0, 1, 2, 3, 4, 5]
        # sorts = ['date', 'likes', 'views', 'answerd', 'notAnswerd']
        sort = 'date'

        index=0
        for category in categorys:
            if index==0:
                questions = Question.objects.filter(category=category, answerd=False).exclude(autor=request.user)
            else:
                index+=1
                question = Question.objects.filter(category=category, answerd=False).exclude(autor=request.user)
                questions.union(question)

        if sort == 'date':
            communication_list = questions.order_by('-date')
        elif sort == 'likes':
            communication_list = questions.order_by('-recommend')
        elif sort == 'views':
            communication_list = questions.order_by('-views')
        elif sort == 'answerd':
            communication_list = questions.filter(answerd=True).order_by('-date')
        else:
            communication_list = questions.filter(answerd=False).order_by('-date')
    else:
        communication_list = Question.objects.filter(answerd=False).exclude(autor=request.user).order_by("-date")
    context = {
        'communication_list': communication_list,
    }
    return render(request, 'communicationApp/answer.html', context)


#내가 한 질문 : my_question
def my_question(request):
    if request.method == 'POST':
        categorys = [0, 1, 2, 3, 4, 5]
        # sorts = ['date', 'likes', 'views', 'answerd', 'notAnswerd']
        sort = 'date'

        index=0
        for category in categorys:
            if index==0:
                questions = Question.objects.filter(category=category, autor=request.user)
            else:
                index+=1
                question = Question.objects.filter(category=category, autor=request.user)
                questions.union(question)

        if sort == 'date':
            communication_list = questions.order_by('-date')
        elif sort == 'likes':
            communication_list = questions.order_by('-recommend')
        elif sort == 'views':
            communication_list = questions.order_by('-views')
        elif sort == 'answerd':
            communication_list = questions.filter(answerd=True).order_by('-date')
        else:
            communication_list = questions.filter(answerd=False).order_by('-date')
    else:
        communication_list = Question.objects.filter(autor=request.user).order_by("-date")
    context = {
        'communication_list': communication_list,
    }
    return render(request, 'my_question.html', context)

#내가 한 답변 : my_answer
def my_answer(request):
    my_answer = Question.objects.all().order_by('-date')
    context = {
        'my_answer': my_answer
    }
    return render(request, 'communicationAPP/my_answer.html', context)

#질문하기 작성할 때 : question_create
def question_create(request):
    if request.method == 'POST':
        question = Question(author=request.user,
                            title=request.POST['title'],
                            category=request.POST['category'],
                            content=request.POST['content'],)
        question.save()
        return redirect('communicationApp:communcation')
    else:
        return render(request, 'communicationAPP/question_create.html')

#답변하기 작성할 때 : answer_create
def answer_create(request, q_id):
    if request.method == 'POST':
        answer = Answer(author=request.user,
                        content=request.POST['content'],)
        answer.save()
        return redirect('communicationApp:answer')
    else:
        return render(request, 'communicationAPP/answer_create.html')

#답변하기 추천 기능 : answer_recommend
def answer_recommend(request, answer_id):
    return render(request, 'answer_recommend.html')

def test(request):
    return render(request, 'communicationApp/question-detail.html')
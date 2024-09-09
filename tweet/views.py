from django.shortcuts import render # type: ignore
from .models import Tweet
from .forms import TweetForm, userRegisterationForm
from django.shortcuts import get_object_or_404,redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth import login # type: ignore
# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweetList.html',{'tweets':tweets})
@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False) 
            tweet.user = request.user
            tweet.save()
            return redirect('tweetList')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form':form})

@login_required
def edit_tweet(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user=request.user)
    if(request.method == 'POST'):
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweetList')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form':form})
@login_required
def delete_tweet(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweetList')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})

def register(request):
    if request.method == 'POST':
        form = userRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweetList')
    else:
        form = userRegisterationForm()
    return render(request, 'registration/register.html', {'form':form})    
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Animes
from .forms import AnimeSearchForm

# form要素を返すanime_search関数を作成
def anime_search(request):
    form = AnimeSearchForm(request.GET)
    return render(request, 'pages/index.html', {'form': form})


# 検索条件に合致するアニメを返すanime_recommendation関数を作成
def anime_recommendation(request):
    form = AnimeSearchForm(request.GET)
    results = Animes.objects.all()

    # フォームの入力値を取得
    if form.is_valid():
        genres = form.cleaned_data['genres']
        episodes = form.cleaned_data['episodes']
        start_date = form.cleaned_data['start_date']

        # 検索条件に合致するアニメを取得
        query = Q()
        if genres:
            query &= Q(genres__contains=genres) # ジャンルが一致するアニメを取得
        if episodes == '物語は長いほうが好き': # エピソード数で絞り込み
            query &= Q(episodes__gt=50)
        elif episodes == '物語は短いほうが好き':
            query &= Q(episodes__lte=50)
        if start_date == '2000年代': # 放送開始年代で絞り込み
            query &= Q(start_date__gte='2000-01-01', start_date__lte='2009-12-31')
        elif start_date == '2010年代':
            query &= Q(start_date__gte='2010-01-01')
        elif start_date == '1990年代':
            query &= Q(start_date__lte='1999-12-31')

        results = results.filter(query).order_by('-rating') # 評価の高い順に並び替え

    # ページネーション
    paginator = Paginator(results, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 表示するページ範囲を限定
    index = page_obj.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 10 if index >= 10 else 0
    end_index = index + 10 if index <= max_index - 10 else max_index
    page_range = paginator.page_range[start_index:end_index]

    return render(request, 'pages/results.html', {'page_obj': page_obj, 'form': form, 'page_range': page_range})


# アニメの詳細情報を返すanime_detail関数を作成
def anime_detail(request, id):
    anime = Animes.objects.get(id=id)
    return render(request, 'pages/detail.html', {'anime': anime})
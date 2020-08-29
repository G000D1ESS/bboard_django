from django.shortcuts import render, redirect
from django.views.generic import ListView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .forms import BbForm, ImgForm
from .models import Bb, Rubric


def add_image(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bboard:index')
    else:
        form = ImgForm()

    context = {
        'form': form,
        'rubrics': Rubric.objects.all()
    }

    return render(request, 'bboard/add_image.html', context)


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


class BbByRubricView(ListView):
    context_object_name = 'bbs'
    template_name = 'bboard/by_rubric.html'

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbCreateView(CreateView):
    form_class = BbForm
    success_url = '/detail/{id}'
    template_name = 'bboard/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def post(self, request, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = '/'
    template_name = 'bboard/bb_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbRedirectView(RedirectView):
    url = '/detail/%(pk)d'

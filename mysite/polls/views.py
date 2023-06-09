from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import pandas as pd
from .models import Choice, Question

pagina = "leeg"


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
        if question_id == 1:
            pagina = "polls/detailRegio.html"
            print("You chose option 1.")
        elif question_id == 2:
            pagina = "polls/detailKlanten.html"
            print("You chose option 2.")
        elif question_id == 5:
            pagina = "polls/detailLeveranciers.html"
            print("You chose option 5.")
        elif question_id == 3:
            pagina = "polls/DetailProducten.html"
            print("You chose option 3.")
        elif question_id == 4:
            pagina = "polls/DetailMedewerkers.html"
            print("You chose option 4.")
        else:
            print("Invalid option.")
            pagina = "polls/detail.html"
 
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
            return render(
                request,
                pagina,
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes += 1
            selected_choice.save()
            
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

class dashboards():
    def regio(request):
        sales_order = pd.read_csv('sales_order.csv')
        sales_order_item = pd.read_csv('sales_order_item.csv')
        product = pd.read_csv('product.csv')
        
        merged_data = pd.merge(sales_order_item, product, left_on='prod_id', right_on='id')
        merged_data = pd.merge(merged_data, sales_order[['id', 'region']], left_on='id_x', right_on='id')
        sales_per_region = merged_data.groupby('region')['id'].count().reset_index()
        sales_per_region.rename(columns={'id': 'total_product_sales'}, inplace=True)
        
        amount_per_region = merged_data.groupby('region')['unit_price'].sum().reset_index()
        amount_per_region.rename(columns={'unit_price': 'total_sales_amount'}, inplace=True)
        
from django.shortcuts import render
from .models import *



class General:
    def base(request):
        ctx = {
        "data_last" : "data_last FROM THE SERVER"
        }
        return render(request,"donation_app/base.html" , ctx)

    #loginrequired
    def streamer_analytics(request):
        user = request.user
        streamer =  Streamer.objects.filter(user = user)[0]
        st_donations = streamer.donation_set.all()

        data_last = []
        labels_last = []
        for donation in st_donations:
            data_last.append(donation.price)
            labels_last.append(donation.date_created.strftime(" %d.%m %H:%M"))

        # data_last = [6,3,1,8,6,3]
        # labels_last = ["day1", "day2","day3","day4","day5","day6"]
        ctx = {
        "data_last":data_last,
        "labels_last":labels_last,
        "data_sum":data_last,
        "labels_sum":labels_last,
        }
        return render(request, "donation_app/streamer_analytics.html", ctx)




# class Donation:
#     def create_donation(request):

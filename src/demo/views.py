# import imp
# from types import TracebackType
# from django.shortcuts import render

# # Create your views here.
# from .views import * 
# from .serializers import * 
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# SENTRY_DSN = "https://26e002f04d774e239032d10feb5ed047@sentry.emtropy.com/4"
# # SENTRY_DSN="http://65c595ed25fa4701bf0af9f2435b4cf2@ec2-3-134-216-137.us-east-2.compute.amazonaws.com/5"
# import os
# import logging
# from typing import Dict
# import sentry_sdk  # type: ignore
# from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration  # type: ignore
# from sentry_sdk.integrations.logging import LoggingIntegration  # type: ignore
# # SENTRY_DSN = os.environ.get('SENTRY_DSN')
# from sentry_sdk.integrations.django import DjangoIntegration

# sentry_sdk.init(
#     dsn=SENTRY_DSN,
#     integrations=[
#         DjangoIntegration()
#     ],
#     environment="staging"
# )

# event ={'name':"deep", "age": 29}
# logger = logging.getLogger(__name__)
# # logger.setLevel(logging.INFO)
# # entry point
# def handle_sentry_issue(event: Dict) -> Dict:
#     import pdb;pdb.set_trace()
#     logger.error("custom error----")
# #     logger.warn("====================================")
# #     division_by_zero = 1 / 0
# #     if division_by_zero:
# #         pass
#     return {
#         'statusCode': 200,
#     }
# # data= {
# #        "new":"new"
# # }

# class BlogApiView(APIView):

#     def get(self, request):
#          blog_obj = Blog.objects.all()
#          serial = BlogSerializers(blog_obj, many = True)
#          handle_sentry_issue(event)
#          return Response(serial.data, status=status.HTTP_200_OK)


#     def post(self, request):
       
#         serial = BlogSerializers(data = request.data)

#         if  serial.is_valid():
#                 serial.save()
#                 return Response(serial.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST )



# class AuthorApiView(APIView):

#     def get(self, request):
#          blog_obj = Blog.objects.all()
#          serial = AuthorSerializers(blog_obj, many = True)
#          return Response(serial.data, status=status.HTTP_200_OK)


#     def post(self, request):
#         serial = AuthorSerializers(data =  request.data)
#         if  serial.is_valid:
#             serial.save()
#             return Response(serial.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST )
# """"
#  with connections['replica'].cursor() as cursor:
#                     list_tickets = []
#                     cursor.execute( request_props["search_path"] )
                    
#                     if ("aspect" in body) and ("behaviour" in body):
#                         if "replies" in body:
#                             query= "select array_agg(reply) from (SELECT distinct t.id as reply  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {2} {4} where ta.status = 1 and t.status in (1,2) and ta.agent_id = {0} {1}   {3}) rp".format( self.reference_id,filters, inner_filter, having_filter, skill_filter)
#                             # query= "select array_agg(reply) from (SELECT distinct t.id as reply  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {4} {6} where ta.status = 1 and t.status in (1,2) and ta.agent_id = {0} and obj->>'name' in {1} and obj->>'sentiment' in {2} {3} {5}) rp".format( self.reference_id, aspects, sentiments, filters, inner_filter, having_filter, skill_filter)
#                             cursor.execute(query)
#                         else:
#                             query= "SELECT array_agg(distinct t.id)  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id {2}  inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {4} where ta.status = 1 and t.status in (1,2) and ta.agent_id = {0}  {1}  {3}".format( self.reference_id,filters, inner_filter, having_filter, skill_filter)
#                             # query= "SELECT array_agg(distinct t.id)  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id {4}  inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {6} where ta.status = 1 and t.status in (1,2) and ta.agent_id = {0} and obj->>'name' in {1} and obj->>'sentiment' in {2} {3} {5}".format( self.reference_id, aspects, sentiments, filters, inner_filter, having_filter, skill_filter)
#                             cursor.execute(query)
    
#                     elif ("aspect" in body) and (body['aspect']):
#                         if "replies" in body:
#                             query = "select array_agg(reply) from (SELECT distinct t.id as reply   FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {2} {4} where t.status in (1,2) and ta.status = 1 and ta.agent_id = {0}  {1}  {3}) rp".format( self.reference_id, filters, inner_filter, having_filter, skill_filter)
#                             cursor.execute(query)
#                             # query = "select array_agg(reply) from (SELECT distinct t.id as reply   FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {4} {6} where t.status in (1,2) and ta.status = 1 and ta.agent_id = {0} and obj->>'name' in {1} and obj->>'sentiment' in {2} {3} {5}) rp".format( self.reference_id, aspects, sentiments, filters, inner_filter, having_filter, skill_filter)
#                             # cursor.execute(query)
#                         else:
#                             query= "SELECT array_agg(distinct t.id)  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {2} {4} where t.status in (1,2) and ta.status = 1 and ta.agent_id = {0}  {1} {3}".format( self.reference_id, filters, inner_filter, having_filter, skill_filter)
#                             # query= "SELECT array_agg(distinct t.id)  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {4} {6} where t.status in (1,2) and ta.status = 1 and ta.agent_id = {0} and obj->>'name' in {1} and obj->>'sentiment' in {2} {3} {5}".format( self.reference_id, aspects, sentiments, filters, inner_filter, having_filter, skill_filter)
#                             cursor.execute(query)
    
                    
#                     elif ("behaviour" in body) and (body['behaviour']):
#                         if "replies" in body:
#                             query="select array_agg(reply) from (SELECT distinct t.id as reply  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {2}  and t.status in (1,2) {4} where ta.status = 1 and ta.agent_id = {0} and {1} {3}) rp".format( self.reference_id,filters, inner_filter, having_filter, skill_filter)
#                             # query="select array_agg(reply) from (SELECT distinct t.id as reply  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {4} {6} and t.status in (1,2), jsonb_array_elements(ta.calc_behaviours) b_obj where ta.status = 1 and ta.agent_id = {0} and b_obj->>'name' in {1} and b_obj->>'sentiment' in {2} {3} {5}) rp".format( self.reference_id, behaviour, sentiments, filters, inner_filter, having_filter, skill_filter)
#                             cursor.execute(query)
#                         else:
#                             query="SELECT array_agg(distinct t.id)  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id  inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {2}  and t.status in (1,2) {4} where ta.status = 1 and ta.agent_id = {0}  {1}   {3}".format( self.reference_id, filters, inner_filter, having_filter, skill_filter)
                            
#                             # query="SELECT array_agg(distinct t.id)  FROM tickets_ticketagent as ta inner join tickets_ticket as t on t.reference_id = ta.ticket_id  inner join tickets_ticketscorecard ts on t.reference_id= ts.ticket_id {4} {6} and t.status in (1,2), jsonb_array_elements(ta.calc_behaviours) b_obj where ta.status = 1 and ta.agent_id = {0} and b_obj->>'name' in {1} and b_obj->>'sentiment' in {2} {3} {5}".format( self.reference_id, behaviour, sentiments, filters, inner_filter, having_filter, skill_filter)
#                             cursor.execute(query)
#                     # list_tickets = cursor.fetchone()[0]


# """

# def post(self,request,key):
#         assignment_data = AssignmentData.objects.get(refkey=key)
#         assignment = Assignment.objects.filter(assignmentdata=assignment_data)
#         reviewee = [i for i in Agent.objects.filter(user_id__in =assignment.values_list('reviewee',flat=True)).values_list('reference_id',flat=True)] 
#         reviewer = [i for i in AssignmentReviewer.objects.filter(assignmentdata=assignment_data).values_list('reviewer',flat=True)]
#         now = datetime.datetime.now()+datetime.timedelta(days=1)
#         body = json.loads(request.body)
#         body['name']=assignment_data.name + '- clone'
#         body["scoring_type"]=assignment_data.scoring_type
#         body["frequency"]=assignment_data.frequency
#         body["due_date"]=assignment_data.due_date.strftime("%Y-%m-%d %H:%M:%S+00") if assignment_data.due_date  else None
#         body["category"]=assignment[0].category
#         body["group_name"]=assignment[0].group_name
#         body["subgroup"]=assignment[0].subgroup
#         body["reviewer"]=reviewer
#         body["reviewee"]=reviewee
#         body["start_date"]=assignment_data.start_date.strftime("%Y-%m-%d") if assignment_data.start_date else None
#         body["end_date"]=assignment_data.end_date.strftime("%Y-%m-%d") if assignment_data.end_date else None
#         body["no_of_interaction"]=assignment[0].no_of_interaction
#         body["channels"]=assignment_data.channels
#         if assignment_data.form_type != "Grading":
#             body["scorecard"]=assignment_data.scorecard.id if assignment_data.scorecard else None 

#         if assignment_data.form_type == "QA":
#             body["schedule_time"]= assignment_data.schedule_time.strftime("%a, %d %b %Y %H:%M:%S GMT") if assignment_data.schedule_time else  now.strftime("%a, %d %b %Y %H:%M:%S GMT")
#             body["participant"]=assignment[0].category
#             body["participant_group"]=assignment[0].group_name
#             body["participant_subgroup"]=assignment[0].subgroup
#             body["recurrence_enddate"]=assignment_data.recurrence_enddate.strftime("%Y-%m-%d %H:%M:%S+00") if assignment_data.recurrence_enddate else None 
#             body["recurrence_date"]=assignment_data.recurrence_date.strftime("%Y-%m-%d %H:%M:%S+00") if assignment_data.recurrence_date else None

#         elif assignment_data.form_type in ("Calibration","Grading"):
#             tickets=[]
#             if assignment[0].category=='By Ticket':
#                 ticket_id = TicketStatus.objects.filter( ticketassignment__assignment__assignmentdata__refkey=key).first().ticket_id
#                 ticket = Ticket.objects.filter(id=ticket_id).first().reference_id
#                 tickets.append(ticket)
                
#             body['tickets'] = tickets
#             body['recurrence']=assignment_data.recurrence if assignment_data.recurrence else None
#             body["recurrence_date"]=assignment_data.recurrence_date.strftime("%Y-%m-%d") if assignment_data.recurrence_date else None

#         else:
#             pass
#         request.body=json.dumps(body).encode('utf-8')
#         if assignment_data.form_type == "QA":
#             demo = AssignmentApi()
#             data = demo.post(request)
#         elif assignment_data.form_type == 'Calibration':
#             demo = CalibrateApi()
#             data = demo.post(request)
#         else:
#             demo = CreateGradingApi()
#             data = demo.post(request)
#         if data.status_code==404:
#                     return Response({"message": "Not Enough Tickets"}, status=st.HTTP_404_NOT_FOUND)
#         elif data.status_code == 201:
#             return JsonResponse({'success': 'Assignment Created Succesfully'}, status=st.HTTP_201_CREATED)
#         else:
            
#             return JsonResponse({'error': 'Invalid data'}, status=st.HTTP_406_NOT_ACCEPTABLE)
#     #   QA
#         # request = {"name":"test","scoring_type":"Ticket","frequency":"One Time","schedule_time":"Mon, 26 Dec 2022 07:10:07 GMT","due_date":"2022-12-27 12:38:59+00","recurrence_date":null,"recurrence_enddate":null,"category":"By Group","group_name":["Team Arnab "],"subgroup":[36],"reviewer":[129],"reviewee":[360750995096],"start_date":"2022-12-01","end_date":"2022-12-26","no_of_interaction":2,"channels":[],"scorecard":10,"participant":"By Group","participant_group":["Team Arnab "],"participant_subgroup":[36]}
# #   calibrate
#         # {"name":"test 34","scoring_type":"Comment","frequency":"Recurring","due_date":"2022-12-28 14:34:52+00","recurrence":"Weekly","recurrence_date":"2022-12-02","category":"By Ticket","group_name":[],"subgroup":[],"reviewer":[129],"reviewee":[],"start_date":null,"end_date":null,"no_of_interaction":null,"channels":[],"scorecard":10,"tickets":[2689238]}
        
#         # {"name":"test 5","scoring_type":"Ticket","frequency":"One Time","due_date":"2022-12-27 14:37:30+00","recurrence":null,"recurrence_date":null,"category":"By Staff","group_name":[],"subgroup":[],"reviewer":[129],"reviewee":[4463090315663],"start_date":"2022-12-01","end_date":"2022-12-27","no_of_interaction":1,"channels":[],"scorecard":1,"tickets":[]}
        
#         # {"name":"ticket ","scoring_type":"Comment","due_date":"2022-12-29 16:35:09+00","frequency":"Recurring","recurrence":"Weekly","recurrence_date":"2022-12-20","category":"By Ticket","group_name":[],"subgroup":[],"reviewer":[129],"reviewee":[],"start_date":null,"end_date":null,"no_of_interaction":null,"channels":[],"tickets":[2604285]}
        
#         # grade
#         # {"name":"clone grage","scoring_type":"Ticket","due_date":"2022-12-28 16:29:36+00","frequency":"One Time","recurrence":null,"recurrence_date":null,"category":"By Grader","group_name":[],"subgroup":[],"reviewer":[129],"reviewee":[100],"start_date":"2022-11-01","end_date":"2022-11-30","no_of_interaction":2,"channels":[],"tickets":[]}
        
#         # {"name":"ticket ","scoring_type":"Comment","due_date":"2022-12-29 16:35:09+00","frequency":"Recurring","recurrence":"Weekly","recurrence_date":"2022-12-20","category":"By Ticket","group_name":[],"subgroup":[],"reviewer":[129],"reviewee":[],"start_date":null,"end_date":null,"no_of_interaction":null,"channels":[],"tickets":[2604285]}
# =========
#             return Response({'message':e},status=st.HTTP_403_FORBIDDEN)
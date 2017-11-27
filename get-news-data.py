#! /usr/bin/env python3
import psycopg2

dbname = "news"
q1 = "What are the most popular three articles of all time?"
q2 = "Who are the most popular article authors of all time?"
q3 = "On which days did more than 1% of requests lead to errors?"

q1_query = (
            "select a.title,count(*) as views from articles a,"
            "log l where l.path like concat('%',a.slug,'%')"
            "and l.status  like '%OK%' group by a.title order by"
            " views desc limit 3")

q2_query = (
             "select au.name,count(*) as views from articles a,"
             "authors au,log l where a.author = au.id and "
             "l.path like concat('%',a.slug,'%')and l.status = '200 OK'"
             "group by au.name order by views desc")

q3_query = (
             "select date , errpercent from ("
             "select date,round(sum(errors)/ (select count(*) from log "
             "where date(time)= date)*100,2) as errpercent from (select"
             " date(time) as date,count(*) as errors from log where "
             "status like '%404%' group by date) as inner_query "
             "group by date order by errpercent desc) as outer_query "
             "where errpercent >1 ")
try:
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    print(q1)
    c.execute(q1_query)
    print("Executed Query 1")
    result1 = c.fetchall()
    for i in range(len(result1)):
        print(result1[i][0], "\t", str(result1[i][1]), " views")
    print(q2)
    c.execute(q2_query)
    print("Executed Query 2")
    result2 = c.fetchall()
    for i in range(len(result2)):
        print(result2[i][0], "\t", str(result2[i][1]), " views")
    print(q3)
    c.execute(q3_query)
    print("Executed Query 3")
    result3 = c.fetchall()
    for i in range(len(result3)):
        print(str(result3[i][0]), "\t", str(result3[i][1]), " % error")
    db.close()
except Exception as e:
    print (e)

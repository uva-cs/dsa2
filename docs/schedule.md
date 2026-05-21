---
layout: default 
title: Schedule
nav_order: 5
---

# Semester Schedule

The schedule will be flexible as we cover each topic. We might spend some extra time on topics, so we will update the schedule as we progress through the semester.


{% assign curday = site.data.config.firstday | date: "%s" | plus: 18010 %}
{% assign curdayweek = curday | date: "%a" %}
{% assign curdate = curday | date: "%Y-%m-%d" %}
{% assign lastday = site.data.config.lastday | date: "%s" | plus: 18010 %}

{% assign skipone = 86400 %} <!-- M-Tu or Tu-W or ... -->
{% assign skiptwo = 172800 %} <!-- M-W or W-F or Tu-Th -->
{% assign skipthree = 259200 %} <!-- F-M -->
{% assign skipfive = 432000 %} <!-- Th-Tu -->

<table class="schedtab"><thead>
<tr>
    <th>Mtg</th>
    <th>Date</th>
    <th>Topic</th>
    <th>Deadlines</th>
    </tr>
    </thead>
    <tbody><!--  {% increment lab %} {% increment mtg %} -->
{% for day in site.data.schedule %}
    {% for exam in site.data.config.exams %}
      {% assign holday = exam.date | date: "%s" | plus: 18010 %}
      {% if holday == curday %}
        <tr class="exam">
        <td class="exam mtg">{{ curdayweek }}</td>
        <td class="text-center sched">{{exam.date | date: "%m/%d/%Y"}}</td>
        <td class="sched">{{ exam.name }}</td>
        <td class="sched"></td>
        </tr>
        {% if site.data.config.meetingdays == 'MWF' and curdayweek == 'Fri' %}
        {% assign curday = curday | plus: skipthree %}
        {% elsif site.data.config.meetingdays == 'TT' and curdayweek == 'Thu' %}
        {% assign curday = curday | plus: skipfive %}
        {% else %}
        {% assign curday = curday | plus: skiptwo %}
        {% endif %}
        {% assign curdayweek = curday | date: "%a" %}
        {% assign curdate = curday | date: "%Y-%m-%d" %}
      {% endif %}
    {% endfor %}
    {% for holiday in site.data.config.holidays %}
      {% assign holday = holiday.date | date: "%s" | plus: 18010 %}
      {% if holday == curday %}
        <tr class="holiday">
        <td class="holiday mtg">{{ curdayweek }}</td>
        <td class="text-center sched">{{holiday.date | date: "%m/%d/%Y"}}</td>
        <td class="sched">{{ holiday.name }}</td>
        <td class="sched"></td>
        </tr>
        {% if site.data.config.meetingdays == 'MWF' and curdayweek == 'Fri' %}
        {% assign curday = curday | plus: skipthree %}
        {% elsif site.data.config.meetingdays == 'MWF' and curdayweek == 'Tue' %}
        {% assign curday = curday | plus: skipone %}
        {% elsif site.data.config.meetingdays == 'MWF' and curdayweek == 'Thu' %}
        {% assign curday = curday | plus: skipone %}
        {% elsif site.data.config.meetingdays == 'TT' and curdayweek == 'Thu' %}
        {% assign curday = curday | plus: skipfive %}
        {% else %}
        {% assign curday = curday | plus: skiptwo %}
        {% endif %}
        {% assign curdayweek = curday | date: "%a" %}
        {% assign curdate = curday | date: "%Y-%m-%d" %}
      {% endif %}
    {% endfor %}
    {% for lab in site.data.config.labs %}
      {% assign holday = lab.date | date: "%s" | plus: 18010 %}
      {% if holday == curday %}
        <tr class="lab">
        <td class="lab mtg">LAB {% increment lab %}</td>
        <td class="text-center sched">{{lab.date | date: "%m/%d/%Y"}}</td>
        <td class="sched">{{ lab.topic }}</td>
        <td class="sched"></td>
        </tr>
        {% if site.data.config.meetingdays == 'MWF' and curdayweek == 'Tue' %}
        {% assign curday = curday | plus: skipone %}
        {% elsif site.data.config.meetingdays == 'MWF' and curdayweek == 'Thu' %}
        {% assign curday = curday | plus: skipone %}
        {% elsif site.data.config.meetingdays == 'TT' and curdayweek == 'Thu' %}
        {% assign curday = curday | plus: skipfive %}
        {% else %}
        {% assign curday = curday | plus: skiptwo %}
        {% endif %}
        {% assign curdayweek = curday | date: "%a" %}
        {% assign curdate = curday | date: "%Y-%m-%d" %}
      {% endif %}
    {% endfor %}
    {% for holiday in site.data.config.holidays %}
      {% assign holday = holiday.date | date: "%s" | plus: 18010 %}
      {% if holday == curday %}
        <tr class="holiday">
        <td class="holiday mtg">{{ curdayweek }}</td>
        <td class="text-center sched">{{holiday.date | date: "%m/%d/%Y"}}</td>
        <td class="sched">{{ holiday.name }}</td>
        <td class="sched"></td>
        </tr>
        {% if site.data.config.meetingdays == 'MWF' and curdayweek == 'Fri' %}
        {% assign curday = curday | plus: skipthree %}
        {% elsif site.data.config.meetingdays == 'MWF' and curdayweek == 'Tue' %}
        {% assign curday = curday | plus: skipone %}
        {% elsif site.data.config.meetingdays == 'MWF' and curdayweek == 'Thu' %}
        {% assign curday = curday | plus: skipone %}
        {% elsif site.data.config.meetingdays == 'TT' and curdayweek == 'Thu' %}
        {% assign curday = curday | plus: skipfive %}
        {% else %}
        {% assign curday = curday | plus: skiptwo %}
        {% endif %}
        {% assign curdayweek = curday | date: "%a" %}
        {% assign curdate = curday | date: "%Y-%m-%d" %}
      {% endif %}
    {% endfor %}
    {% if day.type == 'holiday' or day.type == 'labholiday' %}
    <tr class="holiday">
    {% elsif day.type == 'header' %}
    <tr class="header">
    {% elsif day.type == 'lab' %}
    <tr class="lab">
    {% elsif day.type == 'exam' %}
    <tr class="exam">
    {% else %}
    <tr>
    {% endif %}
    {% if day.type == 'lab' %}
    <td class="lab mtg">LAB {% increment lab %}
    {% elsif day.type == 'header'%}
    <td class="header mtg">
    {% elsif day.type == 'holiday'%}
    <td class="holiday mtg">
    {% elsif day.type == 'labholiday'%}
    <td class="holiday mtg">LAB
    {% elsif day.type == 'exam'%}
    <td class="exam mtg"> {{day.date | date: "%a"}}
    {% else %}
    <td class="mtg">
      {{ curdayweek }}
    {% endif %}</td>
    <td class="text-center sched">
    {% if day.type != 'header' %}
    {% if day.date %} {{ day.date }} {% else %}
    {{curday | date: "%m/%d/%Y"}}
    {% endif %}
    {% endif %}
    </td>
    <td class="sched">
    {% if day.link %}
        <a href="{{day.link}}">
    {% endif %}
    {{day.topic}}
    {% if day.link %}
        </a>
    {% endif %}
    {% if day.lectures or day.readings %}
    <br><span class="sched-sub">
        {% if day.readings %}
        Readings &amp; Resources:
        {% for read in day.readings %}
        {% unless forloop.first %}
        -
        {% endunless %}
        <a href="{{read.link}}">{{read.topic}}</a> 
        {% endfor %}
        {% endif %}
        {% if day.supplements and day.readings %}
        <br>
        {% endif %}
        {% if day.supplements %}
        Supplements:
        {% for read in day.supplements %}
        {% unless forloop.first %}
        -
        {% endunless %}
        <a href="{{read.link}}">{{read.topic}}</a> 
        {% endfor %}
        {% endif %}
        {% if day.lectures and day.readings or day.supplements %}
        <br>
        {% endif %}
        {% if day.lectures %}
        Slides:<br>
        {% for pdf in day.lectures %}
        {% unless forloop.first %}
        <br>
        {% endunless %}
        &nbsp;&nbsp;&nbsp;&nbsp;
        {% if pdf.link %}
        <a href="{{pdf.link}}" aria-label="{{day.topic}} - {{pdf.title}}">{{day.topic}} - {{pdf.title}}</a> 
        {% else %}
        <span title="{{pdf.alt}}">{{pdf.title}}</span> 
        {% endif %}
        {% endfor %}
        {% endif %}
        </span>
    {% endif %}
    </td>
    <td class="sched">
    {{day.notes}}
    {% for assgn in site.data.config.assignments %}
    {% assign assigndate = assgn.date | date: "%s" | plus: 18010 %}
    {% if assigndate == curday and day.type != 'header' %}
    {{ assgn.name }}<br>
    {% endif %}
    {% endfor %}
    </td>
    </tr>
    {% if day.type != 'header' %}
        {% if site.data.config.meetingdays == 'MWF' and curdayweek == 'Fri' %}
        {% assign curday = curday | plus: skipthree %}
        {% elsif site.data.config.meetingdays == 'TR' and curdayweek == 'Thu' %}
        {% assign curday = curday | plus: skipfive %}
        {% elsif site.data.config.meetingdays == 'MWF' and curdayweek == 'Mon' and site.data.config.labdays == 'T' %}
        {% assign curday = curday | plus: skipone %}
        {% elsif site.data.config.meetingdays == 'MWF' and curdayweek == 'Wed' and site.data.config.labdays == 'R' %}
        {% assign curday = curday | plus: skipone %}
        {% else %}
        {% assign curday = curday | plus: skiptwo %}
        {% endif %}
    {% endif %}
    {% assign curdayweek = curday | date: "%a" %}
    {% assign curdate = curday | date: "%Y-%m-%d" %}
{% endfor %}
</tbody></table>

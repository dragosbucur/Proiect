#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[16]:


df = pd.read_excel ("D:\Final_Project\Kylian Mbappé.xlsx")#import excel file to workbook
print (df) #insert the data table
df


# In[17]:


#Question(1): Analysis for his number of match, Goaals, and assist over seasons

#transfer the data in the table into a values
Season = df['Season'].values 
Goals = df['Goals'].values
Match = df['Match'].values
Assist = df['Assist'].values
#####################################
print("the seasons is:")
print(Season)
print("the golas is:")
print(Goals)
print("the match is:")
print(Match)
print("the assist is:")
print(Assist)
# plotting a bar chart 

width = 0.40
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(Season, Goals, width,bottom=Match, color='r')
ax.bar(Season, Match, width, color='b')
ax.bar(Season, Assist, width, color='y')
# naming the y-axis
ax.set_ylabel('Numbers')
# naming the x-axis
ax.set_title('Goals & Match')
#arrange of number on x and y axis
ax.set_yticks(np.arange(0, 100, 5))
ax.legend(labels=['Goals', 'Match','Assist'])
# function to show the plot
plt.show()


# In[18]:


#Question(2) Calculate the goals & assists ratio over season

#transfer the data in the table into a values
Time_played = df['Time played (Min)'].values
print("The time played is")
print(Time_played)

#calculate the Assists_ratio depend on Time_played
Assists_ratio = Assist/(Time_played/90)
print("The assist ratio is")
print(Assists_ratio)

#calculate the Goals_ratio depend on Time_played
Goals_ratio = Goals/(Time_played/90)
print("The goal ratio is")
print(Goals_ratio)

# plotting the line 1 points
plt.plot(Season, Assists_ratio, label = "Assists_ratio")

# plotting the line 2 points
plt.plot(Season, Goals_ratio,  label = "Goals_ratio")

# naming the x axis
plt.xlabel('Season')
# naming the y axis
plt.ylabel('Goals_ratio & Assists_ratio')

# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()


# In[19]:


#Question(3) Calculate the shot and pass Accuracy (out of 1)

#Calculate the shot accuracy depend on goals and shot on target

On_Target = df['On Target'].values
Shot_Accuracy = Goals/On_Target #calculate the shot accuracy
print("the shot accuracy is:")
print(Shot_Accuracy)

#Calculate the pass accuracy depend on compleated pass
Pass = df['Passes'].values
completed_pass = df['Completed Passes'].values
Pass_Accuracy = completed_pass/Pass #calculate the pass accuracy
print("the pass accuracy is:")
print(Pass_Accuracy) 

# Create a chart for his Pass_Accuracy
plt.plot(Season,Pass_Accuracy,'b-o',label='Pass Accuracy over seasons');

#name x & y axis
plt.xlabel('Season')
plt.ylabel('Accuracy')

# Create a chart for his Shot_Accuracy
plt.plot(Season,Shot_Accuracy,'b-x',label='Shot Accuracy over seasons');

#name x & y axis
plt.xlabel('Season')
plt.ylabel('Accuracy')

# plot a chart
plt.legend()
plt.show()


# In[20]:


# Question (4) calculating the overall rating depend on (goals and assits ratio & shot and pass accuracy) (out of 1)

overall_rating = (Shot_Accuracy * Pass_Accuracy) + (Goals_ratio * Assists_ratio) #froumla that we used 
print(overall_rating)

#create a bar char for overall rating
# create a dataset
height = overall_rating
bars = Season
x_pos = np.arange(len(bars))

# Create bars with different colors
plt.bar(x_pos, height, color=['black', 'red', 'green', 'blue', 'cyan'])

# Create names on the x-axis
plt.xticks(x_pos, bars)

# Show graph
plt.show()


# In[21]:


#add the goals ratio and shot accuracy to the main table
df['Goals_ratio'] = Goals_ratio
df['Shot_Accuracy'] = Shot_Accuracy
df


# In[22]:


# Question (5) calculate the Expected Goals

#calculate the time ratio over seasons
Time_ratio = Time_played/(Match*90) #formula we used
print("the Time_ratio is:")
print(Time_ratio)
df['Time_ratio'] = Time_ratio #add the time ratio to the main table

#calculate X_ratio
X_ratio = Time_ratio * Goals_ratio * Shot_Accuracy
print("the X_ratio is:")
print(X_ratio)
df['X_ratio'] = X_ratio #add the x_ratio to the main table

#calculate y_ratio
y_ratio = (X_ratio * Goals) + (X_ratio * On_Target)
print("the y_ratio is:")
print (y_ratio)
#add the y_ratio into the main table
df['y_ratio'] = y_ratio
#add the percent for each season we use for expected goals, so we use 40% percent from his last season performance and 20% from other seasons performance
percent = [0,0.4,0.2,0.2,0.2]
print(percent)
df['percent'] = percent
print(df)
#############################
new_goals = y_ratio * percent * 0.8 # 0.8 = 1-0.2, 0.2 is a tolerance error 
df['new_goals'] = new_goals # add to the main table
Expected_table = df[['Goals','On Target','Goals_ratio','Shot_Accuracy','Time_ratio','X_ratio','percent','new_goals']].drop([0], axis = 0).head()
Expected_table


# In[23]:


Expected_goals = sum(new_goals) #the last calculation for the expected goals
print("the Expected_goals is:")
print(Expected_goals)


# In[24]:


#Question (6) Market value and overall rating 

marketValue = df['MV'].values #define the market value as a value
df['overall_rating'] = overall_rating #put the overall rating in the main table

#create the chart for overall rating
# data
df = pd.DataFrame({
    'x_axis': Season, 
    'y_axis': overall_rating 
})
 
# plot
fig = plt.figure(figsize=(8,8))
plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o')
plt.show()
#create a chart for market value over seasons
# data
df = pd.DataFrame({
    'x_axis': Season, 
    'y_axis': marketValue 
})
 
# plot
fig = plt.figure(figsize=(8,8))
plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o')
plt.show()


# In[ ]:





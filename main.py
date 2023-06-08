
import math
import numpy as np
from math import factorial

city_size_in_km2 =eval(input("Please enter the city size in km^2 :"))
no_of_users_per_km2 =eval( input ("Please enter the number of users per km^2 :"))
average_no_of_calls_per_day_user =eval( input ("Please enter the average number of calls per day per user :"))
average_call_duration_in_min = eval(input ("Please enter the average call duartion in minutes of users in the city :"))
total_no_of_channels =eval( input ("Please enter the number of channels available for the service provider :"))
max_no_of_channels_supported_by_BS =eval( input("Please enter the maximum number of channels supported by one Base Station :"))
CI = eval(input("Please enter the carrier to interference ratio (C/I) :"))
sectoring_angle =eval( input("Please enter the sectoring angle (10 or 120 or 180 or 360):"))
#blocking_probability = input("Please enter the blocking probability :")
no_of_time_slots =eval( input("Please enter the number of time slots :"))
no_of_time_slots_per_user =eval( input("Please enter the number of time slots :"))
    
three_N_Over_n=np.array([])
N_reuse_factor=1
def erlang_b(A, N):
    
    '''
    Calculates the probability of blocking in an N-channel system with A traffic units(A:average number of arrivals per time period& N represents the number of channels or servers available)
    using the Erlang B formula.
    '''
    
    numerator = (A**N) / math.factorial(N)
    denominator = sum([(A**i) / math.factorial(i) for i in range(N+1)])
    return numerator / denominator



    
    
    
    
    

if sectoring_angle==360:
    no_of_sectors_per_cell = 360/sectoring_angle
    total_no_of_users_in_the_city = city_size_in_km2*no_of_users_per_km2
            
    N_reuse_factor = (CI*6)/3
        
    a_user = (average_no_of_calls_per_day_user/(24*60))*average_call_duration_in_min
    no_of_channels_per_cell = total_no_of_channels/N_reuse_factor 
    no_of_trunks = no_of_channels_per_cell*(no_of_time_slots/no_of_time_slots_per_user)
    no_of_trunks_per_sector = no_of_trunks/no_of_sectors_per_cell
    
    a_sector = erlang_b(average_call_duration_in_min, total_no_of_channels)
    a_cell = a_sector*no_of_sectors_per_cell
    no_of_subscribers_per_cell = a_cell/a_user
    total_no_of_cells_required = total_no_of_users_in_the_city/no_of_subscribers_per_cell
    
    print ("Total number of cells required using 360 sectoring :"  )
    print(int(total_no_of_cells_required))


else:

    if sectoring_angle==10:
        three_N_Over_n=np.array([0,0,0,9,12,0,0,21,0,27,0,0,36,39,0,0,48])
    elif sectoring_angle==120:
        three_N_Over_n=np.array([0,0,0,3,6,0,0,10.5,0,13.5,0,0,18,19.5,0,0,24])
    elif sectoring_angle==180:
        three_N_Over_n=np.array([0,0,0,2.25,4,0,0,7,0,9,0,0,9,13,0,0,16])
    
    for i in three_N_Over_n:
        if (i>=CI):
            CI=i
            N_reuse_factor=np.where(three_N_Over_n==i)[0]
            break
        
        
    no_of_sectors_per_cell = 360/sectoring_angle
    total_no_of_users_in_the_city = city_size_in_km2*no_of_users_per_km2
            
            
    a_user = (average_no_of_calls_per_day_user/(24*60))*average_call_duration_in_min
    no_of_channels_per_cell = total_no_of_channels/N_reuse_factor 
    no_of_trunks = no_of_channels_per_cell*(no_of_time_slots/no_of_time_slots_per_user)
    no_of_trunks_per_sector = no_of_trunks/no_of_sectors_per_cell
            
    a_sector = erlang_b(average_call_duration_in_min, total_no_of_channels)
    a_cell = a_sector*no_of_sectors_per_cell
    no_of_subscribers_per_cell = a_cell/a_user
    total_no_of_cells_required = total_no_of_users_in_the_city/no_of_subscribers_per_cell
        
    print ("Total number of cells required using 360 sectoring :" )
    print(int( total_no_of_cells_required))
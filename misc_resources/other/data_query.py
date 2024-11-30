from sqlalchemy import func, distinct

def dummy_data_query (session, dummy_data) :
# Querying for all general information
# All field names (e.g. "dummy_data.id_col") listed within dummy_data_query for ease of use when building other queries
    # beaches_results = session.query(
    dummy_data_results = session.query(
        dummy_data.id_col,
        dummy_data.int_col,
        dummy_data.float_col,
        dummy_data.string_col,
        dummy_data.bool_col,
        dummy_data.na_col,
        dummy_data.time_col,
        dummy_data.latitude_col,
        dummy_data.longitude_col
        ).all()

    dummy_data_array = []
    for dummy_data_info in dummy_data_results:
        dummy_data_array.append({
            "id_col": dummy_data_info[0],
            "int_col": dummy_data_info[1],
            "float_col": dummy_data_info[2],
            "string_col": dummy_data_info[3],
            "bool_col": dummy_data_info[4],
            "na_col": dummy_data_info[5],
            "latitude_col": dummy_data_info[6],
            "longitude_col": dummy_data_info[7]
    })

    return dummy_data_array



def raw_data_query (session, raw_data) :
# Querying for all general beach information (e.g. beach name, ameneties, address)
# All field names (e.g. "Beaches.region") listed within beach_query and beaches_data for ease of use when building other queries
    # beaches_results = session.query(
    raw_data_results = session.query(
        raw_data.index,
        raw_data.Age,
        raw_data.Attrition,
        raw_data.BusinessTravel,
        raw_data.DailyRate,
        raw_data.Department,
        raw_data.DistanceFromHome,
        raw_data.Education,
        raw_data.EducationField,
        raw_data.EmployeeCount,
        raw_data.EmployeeNumber,
        raw_data.EnvironmentSatisfaction,
        raw_data.Gender,
        raw_data.HourlyRate,
        raw_data.JobInvolvement,
        raw_data.JobLevel,
        raw_data.JobRole,
        raw_data.JobSatisfaction,
        raw_data.MaritalStatus,
        raw_data.MonthlyIncome,
        raw_data.MonthlyRate,
        raw_data.NumCompaniesWorked,
        raw_data.Over18,
        raw_data.OverTime,
        raw_data.PercentSalaryHike,
        raw_data.PerformanceRating,
        raw_data.RelationshipSatisfaction,
        raw_data.StandardHours,
        raw_data.StockOptionLevel,
        raw_data.TotalWorkingYears,
        raw_data.TrainingTimesLastYear,
        raw_data.WorkLifeBalance,
        raw_data.YearsAtCompany,
        raw_data.YearsInCurrentRole,
        raw_data.YearsSinceLastPromotion,
        raw_data.YearsWithCurrManager
        ).all()

    raw_data = []
    for raw_data_info in raw_data_results:
        raw_data.append({
        "index": raw_data_info[0],
        "Age": raw_data_info[1],
        "Attrition": raw_data_info[2],
        "BusinessTravel": raw_data_info[3],
        "DailyRate": raw_data_info[4],
        "Department": raw_data_info[5],
        "DistanceFromHome": raw_data_info[6],
        "Education": raw_data_info[7],
        "EducationField": raw_data_info[8],
        "EmployeeCount": raw_data_info[9],
        "EmployeeNumber": raw_data_info[10],
        "EnvironmentSatisfaction": raw_data_info[11],
        "Gender": raw_data_info[12],
        "HourlyRate": raw_data_info[13],
        "JobInvolvement": raw_data_info[14],
        "JobLevel": raw_data_info[15],
        "JobRole": raw_data_info[16],
        "JobSatisfaction": raw_data_info[17],
        "MaritalStatus": raw_data_info[18],
        "MonthlyIncome": raw_data_info[19],
        "MonthlyRate": raw_data_info[20],
        "NumCompaniesWorked": raw_data_info[21],
        "Over18": raw_data_info[22],
        "OverTime": raw_data_info[23],
        "PercentSalaryHike": raw_data_info[24],
        "PerformanceRating": raw_data_info[25],
        "RelationshipSatisfaction": raw_data_info[26],
        "StandardHours": raw_data_info[27],
        "StockOptionLevel": raw_data_info[28],
        "TotalWorkingYears": raw_data_info[29],
        "TrainingTimesLastYear": raw_data_info[30],
        "WorkLifeBalance": raw_data_info[31],
        "YearsAtCompany": raw_data_info[32],
        "YearsInCurrentRole": raw_data_info[33],
        "YearsSinceLastPromotion": raw_data_info[34],
        "YearsWithCurrManager": raw_data_info[35]
    })
    return raw_data

# # Querying for all water quality grade data
# def grades_query (session, Grade_data) :
#     grades_results = session.query(
#         Grade_data.id,
#         Grade_data.json_id,
#         Grade_data.name1,
#         Grade_data.latitude,
#         Grade_data.longitude,
#         Grade_data.address,
#         Grade_data.city,
#         Grade_data.county,
#         Grade_data.state,
#         Grade_data.zip,
#         Grade_data.active,
#         Grade_data.grade_updated,
#         Grade_data.dry_grade,
#         Grade_data.wet_grade,
#         Grade_data.annual_summer_dry,
#         Grade_data.annual_year_wet,
#         Grade_data.annual_winter_dry,
#         Grade_data.annual_year,
#         Grade_data.grade_created
#         ).all()

#     grades_data = []
#     for grades_info in grades_results:
#         grades_data.append({
#             "id": grades_info[0],
#             "json_id": grades_info[1],
#             "name1": grades_info[2],
#             "latitude": grades_info[3],
#             "longitude": grades_info[4],
#             "address": grades_info[5],
#             "city": grades_info[6],
#             "county": grades_info[7],
#             "state": grades_info[8],
#             "zip": grades_info[9],
#             "active": grades_info[10],
#             "grade_updated": grades_info[11],
#             "dry_grade": grades_info[12],
#             "wet_grade": grades_info[13],
#             "annual_summer_dry": grades_info[14],
#             "annual_year_wet": grades_info[15],
#             "annual_winter_dry": grades_info[16],
#             "annual_year": grades_info[17],
#             "grade_created": grades_info[18]
#     })
#     return grades_data


# # Test query/output for early stage development
# # def grades_dummy_query (session, Grade_data_dummy) :
# #     grades_dummy_results = session.query(
# #         Grade_data_dummy.id,
# #         Grade_data_dummy.beach_name,
# #         Grade_data_dummy.latitude,
# #         Grade_data_dummy.longitude,
# #         Grade_data_dummy.date,
# #         Grade_data_dummy.dry_grade,
# #         Grade_data_dummy.wet_grade,
# #         Grade_data_dummy.annual_summer_dry,
# #         Grade_data_dummy.annual_year_wet,
# #         Grade_data_dummy.annual_winter_dry,
# #         Grade_data_dummy.annual_year
# #         ).all()

# #     grades_dummy_data = []
# #     for grades_dummy_info in grades_dummy_results:
# #         grades_dummy_data.append({
# #             "id": grades_dummy_info[0],
# #             "beach_name": grades_dummy_info[1],
# #             "latitude": grades_dummy_info[2],
# #             "longitude": grades_dummy_info[3],
# #             "date": grades_dummy_info[4],
# #             "dry_grade": grades_dummy_info[5],
# #             "wet_grade": grades_dummy_info[6],
# #             "annual_summer_dry": grades_dummy_info[7],
# #             "annual_year_wet": grades_dummy_info[8],
# #             "annual_winter_dry": grades_dummy_info[9],
# #             "annual_year": grades_dummy_info[10]
# #     })

# #     # return grades_dummy_data
# #     return grades_dummy_data


# # Querying for latest beach grade data
# def latest_grades_query (session, Grade_data) :

#     # Subquery to find the latest entry for a beach
#     subq = session.query(func.max(Grade_data.id)).group_by(Grade_data.name1).all()

#     id_list = []
#     for x in subq:
#         id_list.append(x[0])

#     # Query to find the result ids in the full list
#     # Used ".filter()" instead of ".where()" after sqlAlchemy downgrade to 1.3.18
#     query = session.query(Grade_data).filter(Grade_data.id.in_(id_list)).all()

#     latest_grades_data = []
#     for grades_info in query:
#         latest_grades_data.append({
#             "id": grades_info.id,
#             "json_id": grades_info.json_id,
#             "name1": grades_info.name1,
#             "latitude": grades_info.latitude,
#             "longitude": grades_info.longitude,
#             "address": grades_info.address,
#             "city": grades_info.city,
#             "county": grades_info.county,
#             "state": grades_info.state,
#             "zip": grades_info.zip,
#             "active": grades_info.active,
#             "grade_updated": grades_info.grade_updated,
#             "dry_grade": grades_info.dry_grade,
#             "wet_grade": grades_info.wet_grade,
#             "annual_summer_dry": grades_info.annual_summer_dry,
#             "annual_year_wet": grades_info.annual_year_wet,
#             "annual_winter_dry": grades_info.annual_winter_dry,
#             "annual_year": grades_info.annual_year,
#             "grade_created": grades_info.grade_created
#     })

#     return latest_grades_data


# # Query for timelapse map usiing Leaflet-timeline plugin
# def grades_query_geojson (session, Grade_data) :
# # Querying for all grade beach data
#     geojson_grades_results = session.query(
#         Grade_data.id,
#         Grade_data.json_id,
#         Grade_data.name1,
#         Grade_data.latitude,
#         Grade_data.longitude,
#         Grade_data.grade_updated,
#         Grade_data.dry_grade
#         # Find all observations from 2021.01.01
#         ).filter(Grade_data.grade_updated > '2021-01-01').all()

# # Assembling a geoJSON for Leaflet-timeline
#     grades_data = []
#     for grades_info in geojson_grades_results:
#         grades_data.append(
#             {
#             "type":"Feature",
#             "properties":{
#                 "id": grades_info[0],
#                 "json_id": grades_info[1],
#                 "beach_name":grades_info[2],
#                 "grade": grades_info[6],
#                 "time": grades_info[5]
#             },
#             "geometry":{
#                 "type": "Point",
#                 "coordinates":[
#                     grades_info[4],
#                     grades_info[3]
#                 ]
#             }
#     })
#     grades_data_geojson = ({
#         "type": "FeatureCollection",
#         "features": grades_data
#     })
#     return grades_data_geojson


# def unq_years_query (session, Grade_data) :
# # Querying for unique years in grade data
#     grades_results = session.query(
#         distinct(func.date_part('YEAR', Grade_data.grade_updated)))

#     years_data = []
#     for grades_info in grades_results:
#         years_data.append(int(grades_info[0]))

#     years_data.sort()

#     return years_data

# def count_by_year (session, Grade_data, year) :
# # Querying for unique years in grade data

#     grade_values = ["A+", "A", "B", "C", "D", "F"]

#     count_data = []
#     for month in range(1,13):
#         for grade in grade_values:
#             grades_results = (session.query (
#                 func.count(Grade_data.id))
#                 .filter(func.date_part('YEAR', Grade_data.grade_updated) == int(year))
#                 .filter(func.date_part('MONTH', Grade_data.grade_updated) == month)
#                 .filter(Grade_data.dry_grade == grade)).scalar()

#             # append grade, month number, and count of dry grades
#             count_data.append([grade, month, grades_results])
#             session.commit()


#             grades_results = (session.query (
#                 func.count(Grade_data.id))
#                 .filter(func.date_part('YEAR', Grade_data.grade_updated) == int(year))
#                 .filter(func.date_part('MONTH', Grade_data.grade_updated) == month)
#                 .filter(Grade_data.wet_grade == grade)).scalar()

#             # append count of wet grades to list
#             count_data[-1].append(grades_results)
#             session.commit()

#     return count_data


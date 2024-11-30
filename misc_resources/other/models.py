def create_dummy_classes(db):
    class dummy(db.Model):
        __tablename__ = 'dummy_data'
        id_col = db.Column(db.Integer, primary_key=True, autoincrement = True)
        int_col = db.Column(db.String(64))
        float_col = db.Column(db.String(64))
        string_col = db.Column(db.String(64))
        bool_col = db.Column(db.String(64))
        na_col = db.Column(db.String(64))
        time_col = db.Column(db.String(64))
        latitude_col = db.Column(db.String(64))
        longitude_col = db.Column(db.String(64))
        def __repr__(self):
            return '<Dummy %r>' % (self.string_col)
    return dummy


def create_raw_classes(db):
    class raw(db.Model):
        __tablename__ = 'raw_data'
        index = db.Column(db.Integer, primary_key=True)
        Age = db.Column(db.Integer)
        Attrition = db.Column(db.String(64))
        BusinessTravel = db.Column(db.String(64))
        DailyRate = db.Column(db.Integer)
        Department = db.Column(db.String(64))
        DistanceFromHome = db.Column(db.Integer)
        Education = db.Column(db.Integer)
        EducationField = db.Column(db.String(64))
        EmployeeCount = db.Column(db.Integer)
        EmployeeNumber = db.Column(db.Integer)
        EnvironmentSatisfaction = db.Column(db.Integer)
        Gender = db.Column(db.String(64))
        HourlyRate = db.Column(db.Integer)
        JobInvolvement = db.Column(db.Integer)
        JobLevel = db.Column(db.Integer)
        JobRole = db.Column(db.String(64))
        JobSatisfaction = db.Column(db.Integer)
        MaritalStatus = db.Column(db.String(64))
        MonthlyIncome = db.Column(db.Integer)
        MonthlyRate = db.Column(db.Integer)
        NumCompaniesWorked = db.Column(db.Integer)
        Over18 = db.Column(db.String(64))
        OverTime = db.Column(db.String(64))
        PercentSalaryHike = db.Column(db.Integer)
        PerformanceRating = db.Column(db.Integer)
        RelationshipSatisfaction = db.Column(db.Integer)
        StandardHours = db.Column(db.Integer)
        StockOptionLevel = db.Column(db.Integer)
        TotalWorkingYears = db.Column(db.Integer)
        TrainingTimesLastYear = db.Column(db.Integer)
        WorkLifeBalance = db.Column(db.Integer)
        YearsAtCompany = db.Column(db.Integer)
        YearsInCurrentRole = db.Column(db.Integer)
        YearsSinceLastPromotion = db.Column(db.Integer)
        YearsWithCurrManager = db.Column(db.Integer)
        def __repr__(self):
            return '<Dummy %r>' % (self.string_col)
    return raw

# def create_classes(db):
#     class Beach(db.Model):
#         __tablename__ = 'beaches'
#         id = db.Column(db.Integer, primary_key=True)
#         region = db.Column(db.String(64))
#         county = db.Column(db.String(64))
#         area = db.Column(db.String(64))
#         beach_name = db.Column(db.String(64))
#         beach_url = db.Column(db.String(64))
#         address = db.Column(db.String(64))
#         city = db.Column(db.String(64))
#         state = db.Column(db.String(64))
#         zip = db.Column(db.String(64))
#         latitude = db.Column(db.Float(64))
#         longitude = db.Column(db.Float(64))
#         park_name = db.Column(db.String(64))
#         owner = db.Column(db.String(64))
#         owner_url = db.Column(db.String(64))
#         activities = db.Column(db.String(64))
#         amenities = db.Column(db.String(64))
#         pet_policy = db.Column(db.String(64))
#         pets_allowed = db.Column(db.String(1))
#         fees = db.Column(db.String(64))
#         free_parking = db.Column(db.String(1))
#         phone = db.Column(db.String(64))
#         other_names = db.Column(db.String(64))
#         def __repr__(self):
#             return '<Beach %r>' % (self.beach_name)
#     return Beach


# def create_grade_classes(db):
#     class Grade_data(db.Model):
#         __tablename__ = 'grade_data'
#         id = db.Column(db.Integer, primary_key=True)
#         json_id = db.Column(db.Integer)
#         title = db.Column(db.String(64))
#         name1 = db.Column(db.String(64))
#         latitude = db.Column(db.String(64))
#         longitude = db.Column(db.String(64))
#         address = db.Column(db.String(64))
#         city = db.Column(db.String(64))
#         county = db.Column(db.String(64))
#         state = db.Column(db.String(64))
#         zip = db.Column(db.String(64))
#         active = db.Column(db.String(64))
#         grade_updated = db.Column(db.String(64))
#         dry_grade = db.Column(db.String(64))
#         wet_grade = db.Column(db.String(64))
#         annual_summer_dry = db.Column(db.String(64))
#         annual_year_wet = db.Column(db.String(64))
#         annual_winter_dry = db.Column(db.String(64))
#         annual_year = db.Column(db.String(64))
#         grade_created = db.Column(db.String(64))
#         alerts = db.Column(db.String(64))
#         def __repr__(self):
#             return '<Grade_data %r>' % (self.name1)
#     return Grade_data


from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())


class Record(db.Model):
    __tablename__ = 'Record'

    fileID = db.Column(db.String(256), primary_key=True)
    prob = db.Column(db.FLOAT)
    LABEL = db.Column(db.String(64))
    strategy = db.Column(db.String(64))

    def __init__(self, fileid, prob, label, strategy):
        self.fileID = fileid
        self.prob = prob
        self.LABEL = label
        self.strategy = strategy


class Feedback(db.Model):
    __tablename__ = 'Feedback'

    fileID = db.Column(db.String(256), primary_key=True)
    comment = db.Column(db.String(512))

    def __init__(self, fileid, comment):
        self.fileID = fileid
        self.comment = comment


class Info(db.Model):
    __tablename__ = 'Info'

    LABEL = db.Column(db.String(64), primary_key=True)
    brand = db.Column(db.String(64))
    nickname = db.Column(db.String(128))
    origin = db.Column(db.String(512))
    company = db.Column(db.String(512))
    createtime = db.Column(db.String(128))
    cofounder = db.Column(db.String(512))
    site = db.Column(db.String(512))
    about = db.Column(db.Text)









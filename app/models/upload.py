from app.models.db import sql_server


class Upload:

    @staticmethod
    def execute(data, table_name):
        try:
            data.to_sql(table_name, con=sql_server.engine, if_exists='append', index=False)
            return 200, 'OK'
        except Exception as err:
            return 500, str(err)
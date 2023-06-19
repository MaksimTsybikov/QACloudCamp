class TestData:
    existing_post = {
        'userId': 1,
        'id': 1,
        'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
        'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita '
                'et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum '
                'est autem sunt rem eveniet architecto'
    }

    unrelated_existing_params = {
        ('userId', 2),
        ('id', 22),
        ('title', 'optio dolor molestias sit'),
        ('body',
         'voluptatem quisquam iste\nvoluptatibus natus officiis facilis dolorem\nquis quas ipsam\nvel et voluptatum in aliquid')
    }

    non_existing_post = {('userId', 12),
                         ('id', 120),
                         ('title', 'fake test title'),
                         ('body', 'fake test body')}

    invalid_params = {('userId', -32),
                      ('id', 'id'),
                      ('title', 1337),
                      ('body', 456222)}

    existing_id_non_existing_userid = {'userId': 3342345, 'id': 10}

    non_existing_id_existing_userid = {'userId': 10, 'id': 121}

    related_non_existing_data = {'userId': 11,
                                 'title': 'Test title',
                                 'body': 'Test body'}

    related_non_existing_params = {('userId', 13), ('title', 'new test title'), ('body', 'new test body')}

    empty_str_params = {('userId', ''), ('title', ''), ('body', '')}

    none_in_params = {('userId', None), ('title', None), ('body', None)}

    space_in_params = {('userId', ' '), ('title', ' '), ('body', ' ')}

    invalid_data_type_in_params = {('userId', '1'), ('title', 1), ('body', 1)}

    html_in_params = {('userId', '<script>alert(«userId»)</script>',),
                      ('title', '<script>alert(«title»)</script>'),
                      ('body', '<script>alert(«body»)</script>')}

    sql_in_params = {('userId', 'test"; DROP TABLE users; --',),
                     ('title', 'test"; DROP TABLE users; --'),
                     ('body', 'test"; DROP TABLE users; --')}

    # После доработки API необходимо будет проверять, что такого id в базе не существует
    non_existing_id = 1001

    not_valid_id = [-100, '', ' ', 'test', 3.4]

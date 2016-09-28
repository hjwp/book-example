describe("list js", function() {

  beforeEach(function () {
    var form = $(
        '<form id="testform">' +
          '<input name="text" />' +
          '<input type="hidden" name="csrfmiddlewaretoken" value="tokey" />' +
          '<div class="has-error"></div>' +
        '</form>'
        );
    $('body').append(form);
    var table = $('<table id="id_list_table"></table>');
    $('body').append(table);
    jasmine.Ajax.install();

  });
  afterEach(function () {
    $('#testform').remove();
    $('#id_list_table').remove();
    jasmine.Ajax.uninstall();
  });

  describe("hiding errors on input", function() {

    it("should hide errors on keypress", function() {
      window.Superlists.hideErrorsOnInput();
      $('#testform input').trigger('keypress');
      expect( $('.has-error').is(':visible') ).toBe(false);
    });

    it("should not hide errors unnecessarily", function() {
      window.Superlists.hideErrorsOnInput();
      expect( $('.has-error').is(':visible') ).toBe(true);
    });

  });

  describe("retrieving and adding to existing lists via ajax", function() {

    it("should retrieve items via ajax and fill in lists table on page load", function () {
      var url = '/listitemsapi/';
      window.Superlists.startAjax(url);

      expect(jasmine.Ajax.requests.mostRecent().url).toBe(url);

      var rowsJson = JSON.stringify([
          {'id': 101, 'text': 'item 1 text'},
          {'id': 102, 'text': 'item 2 text'},
      ]);

      jasmine.Ajax.requests.mostRecent().respondWith({
        "status": 200,
        "contentType": 'application/json',
        "responseText": rowsJson
      });

      var rows = $('#id_list_table tr');
      expect(rows.length).toEqual(2);
      var row1 = $('#id_list_table tr:first-child td');
      expect(row1.text()).toEqual('1: item 1 text');
      var row2 = $('#id_list_table tr:last-child td');
      expect(row2.text()).toEqual('2: item 2 text');
    });


    it("should intercept form submit and do ajax post", function () {
      var url = '/listitemsapi/';
      window.Superlists.startAjax(url);

      $('input[name="text"]').val('user input');
      $('input[name="csrfmiddlewaretoken"]').val('tokeney');
      $('form#testform').submit();
      var request = jasmine.Ajax.requests.mostRecent();
      expect(request.method).toBe('POST');
      expect(request.data()).toEqual(
        {'text': ['user input'], 'csrfmiddlewaretoken': ['tokeney']}
      );
    });

    it("should repopulate items table after post", function () {
      var url = '/listitemsapi/';
      window.Superlists.startAjax(url);
      $('form#testform').submit();
      jasmine.Ajax.requests.mostRecent().respondWith({
        "status": 201,
        "contentType": 'application/json',
        'responseText': '{}'
      });

      var getRequest = jasmine.Ajax.requests.mostRecent();

      expect(getRequest.url).toBe(url);
      expect(getRequest.method).toBe('GET');

      var rowsJson = JSON.stringify([
          {'id': 101, 'text': 'item 1 text'},
          {'id': 102, 'text': 'item 2 text'},
      ]);

      getRequest.respondWith({
        "status": 200,
        "contentType": 'application/json',
        "responseText": rowsJson
      });

      var rows = $('#id_list_table tr');
      expect(rows.length).toEqual(2);
      var row1 = $('#id_list_table tr:first-child td');
      expect(row1.text()).toEqual('1: item 1 text');
      var row2 = $('#id_list_table tr:last-child td');
      expect(row2.text()).toEqual('2: item 2 text');
    });
  });
});


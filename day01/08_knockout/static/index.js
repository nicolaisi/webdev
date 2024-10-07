// Define the ViewModel
function AppViewModel() {
    var self = this;

    // Observable to hold server data
    self.serverData = ko.observable('');

    // Function to load data via AJAX
    self.loadData = function() {
        $.ajax({
            url: '/data/',
            type: 'GET',
            success: function(response) {
                // Update the observable with data from the server
                console.log(response);
                self.serverData(response['data']);
            },
            error: function() {
                self.serverData('Error loading data');
            }
        });
    };

    // Automatically call loadData every 5 seconds (5000 ms)
    setInterval(self.loadData, 1000);
}

// Apply bindings to make KnockoutJS active
ko.applyBindings(new AppViewModel());

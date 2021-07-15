let payload = {
  // name: '',
  unique: true,
  log_type: 'conversions',
  include_click_fields: false,
  include_conversion_fields: false,
  use_universal_date_format: false,
  is_converting_event: null,
  is_manually_created: null,
  columnKeys: [
    'id',
    'click_id',
    null,
    null,
    null,
    null,
    null,
    null,
    'created_at',
    'click_created_at',
    null,
    'updated_at',
    'advertiser_id',
    'affiliate_id',
    'offer_id',
    'campaign_id',
    null,
    null,
    'is_converting_event',
    null,
    null,
    null,
    'geo_country_code',
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
  ],
  recipients: [
    {
      id: 1049,
      email: 'reshma+debiAff@trackrevenue.com',
      name: 'Debi Affiliate Manager',
    },
  ],
  approval_state: 'approved,pending',
};

fetch('http://yd.test:8080/api/v1/scheduled-reports', {
  headers: {
    accept: 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,ro;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    'x-csrftoken':
      'MSSftq5ARjSBPlt2IUFL3nt7BoEqqvBdUCapmly4xeAvHKBlzXYIptaJLWlfM7NR',
  },
  referrer: 'http://yd.test:8080/logs/conversions',
  referrerPolicy: 'strict-origin-when-cross-origin',
  body: '{"unique":true,"log_type":"conversions","include_click_fields":false,"include_conversion_fields":false,"use_universal_date_format":false,"is_converting_event":null,"is_manually_created":null,"columnKeys":["id","click_id",null,null,null,null,null,null,"created_at","click_created_at",null,"updated_at","advertiser_id","affiliate_id","offer_id","campaign_id",null,null,"is_converting_event",null,null,null,"geo_country_code",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"recipients":[{"id":1049,"email":"reshma+debiAff@trackrevenue.com","name":"Debi Affiliate Manager"}],"approval_state":"approved,pending"}',
  method: 'POST',
  mode: 'cors',
  credentials: 'include',
})
  .then((res) => res.json())
  .then(console.log)
  .catch(console.error);
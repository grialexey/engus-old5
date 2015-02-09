function URLParser(u){
    var path = '',
        query = '',
        hash = '',
        params;
    if (u.indexOf("#") !== -1) {
        hash = u.substr(u.indexOf("#") + 1);
        u = u.substr(0 , u.indexOf("#"));
    }
    if (u.indexOf("?") !== -1) {
        path = u.substr(0 , u.indexOf("?"));
        query = u.substr(u.indexOf("?") + 1);
        params= query.split('&');
    } else {
        path = u;
    }
    return {
        getHref: function() {
            var href = path;
            if (query.length > 0) {
                href = href + '?' + query;
            }
            if (hash.length > 0) {
                href = href + '#' + hash;
            }
            return href;
        },
        getHost: function(){
            var hostexp = /\/\/([\w.-]*)/;
            var match = hostexp.exec(path);
            if (match != null && match.length > 1)
                return match[1];
            return "";
        },
        getPath: function(){
            var pathexp = /\/\/[\w.-]*(?:\/([^?]*))/;
            var match = pathexp.exec(path);
            if (match != null && match.length > 1)
                return match[1];
            return "";
        },
        getHash: function() {
            return hash;
        },
        getParams: function() {
            return params
        },
        getQuery: function() {
            return query;
        },
        setHash: function(value) {
            hash = value;
            return this;
        },
        setParam: function(name, value) {
            if (this.getParams(name)) {

            }
            if (params.length > 0) {
                params = [];
            }
            params.push(name + '=' + value);
            if (query.length > 0) {
                query += "&";
            }
            query += params[params.length];
            return this;
        },
        getParam: function(name) {
            if (params) {
                for (var i = 0; i < params.length; i++) {
                    var pair = params[i].split('=');
                    if (decodeURIComponent(pair[0]) == name)
                        return decodeURIComponent(pair[1]);
                }
            } else {
                return undefined;
            }
        },
        hasParam: function(name){
            if (params) {
                for (var i = 0; i < params.length; i++) {
                    var pair = params[i].split('=');
                    if (decodeURIComponent(pair[0]) == name)
                        return true;
                }
            } else {
                return false;
            }
        },
        removeParam: function(name){
            query = '';
            if (params) {
                var newparams = [];
                for (var i = 0;i < params.length;i++) {
                    var pair = params[i].split('=');
                    if (decodeURIComponent(pair[0]) != name)
                          newparams .push(params[i]);
                }
                params = newparams ;
                for (var i = 0; i < params.length; i++) {
                    if(query.length > 0)
                        query += "&";
                    query += params[i];
                }
            }
            return this;
        }
    }
}
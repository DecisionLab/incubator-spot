//
// Licensed to the Apache Software Foundation (ASF) under one or more
// contributor license agreements.  See the NOTICE file distributed with
// this work for additional information regarding copyright ownership.
// The ASF licenses this file to You under the Apache License, Version 2.0
// (the "License"); you may not use this file except in compliance with
// the License.  You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//

var React = require('react');
const ReactDOMServer = require('react-dom/server');

var GridPanelMixin = require('../../../js/components/GridPanelMixin.react');
var SuspiciousMixin = require('../../../js/components/SuspiciousGridMixin.react.js');
var SpotUtils = require('../../../js/utils/SpotUtils.js');
var SuspiciousStore = require('../stores/SuspiciousStore');

var SuspiciousPanel = React.createClass({
    mixins: [GridPanelMixin, SuspiciousMixin],
    store: SuspiciousStore,
    getDefaultProps: function () {
        return {iterator: SuspiciousStore.ITERATOR};
    }
});

module.exports = SuspiciousPanel;

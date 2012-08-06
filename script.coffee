###
Copyright 2012 Daniel Kinsman

This file is part of Decisive Robot.

Decisive Robot is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Decisive Robot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU General Public License
along with Decisive Robot.  If not, see <http://www.gnu.org/licenses/>.
###

jQuery(document).ready ->
    writeanswer = (ans) ->
        jQuery("#answer").html(ans)
        jQuery("#answer").attr("class", "answered")
        jQuery(".unanswered").attr("class", "none")
        question = jQuery("#question").val()
        questionurl = "/?question=" + encodeURIComponent("#{question}")
        jQuery("#externallink").attr("href", questionurl)
        
    answer = () ->
        question = jQuery("#question").val()
        jQuery.getJSON("/service/?question=#{question}", (data) -> writeanswer(data['answer']))
            
    jQuery("form").submit( (event) ->
        event.preventDefault()
        answer()
        return false )
        
    #set focus to the question box
    jQuery("#question").focus()
            
    # if the browser doesn't support svg, replace svgs with pngs
    if not document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure", "1.1")
        jQuery("#robot").attr("src", "decisiverobot.png")
        jQuery("#speechtick").attr("src", "speechtick.png")

	#if the browser is IE, tell them it is shit
	if jQuery.browser.msie
		alert("Decisive Robot works best on decent browsers like Firefox and Chrome. Don't use Internet Explorer, meatbag.")
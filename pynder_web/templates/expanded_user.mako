<%inherit file="pynder_web:templates/base.mako" />

<%
import dateutil.parser
from pynder_core.tinder import humanized_delta
%>

<div class="page-header">
    <h1></h1>
</div>

<div class="row matches">
    <div id=${user.id} class="col-md-12 col-lg-8 col-lg-offset-2">
        <div class="card match">
            <div class="card-block">
                <h4 class="card-title">
                    <a href="#">
                    ${user.name} - ${user.age}
                    </a>
                </h4>
                <h6 class="card-subtitle">${user.bio}</h6>
                % if user.jobs:
                    <p class="card-text">Jobs: ${", ".join(user.jobs)}</p>
                % endif
                % if user.schools:
                    <p class="card-text">Schools: ${", ".join(user.schools)}</p>
                % endif
                <p class="card-text">
                    <small class="text-muted">
                        ${user._data.get('distance_mi')} miles away
                        - last seen ${humanized_delta(dateutil.parser.parse(user.ping_time))}
                    </small> <!-- idea: maybe some sort of map here? -->
                </p>
            </div>
            <div class="row images">
                % for image in user.photos:
                    <div class="col-xs-6">
                        <img class="img-fluid img-thumbnail user"
                             notsrc="http://placehold.it/600x600"
                             src=${str(image)}>
                    </div>
                % endfor
            </div>
            % if user.instagram_username:
                <a href="${'https://www.instagram.com/{}/'.format(user.instagram_username)}" class="card-link">
                    Instagram: ${user.instagram_username}
                </a>
            % endif
        </div>
    </div>
</div>

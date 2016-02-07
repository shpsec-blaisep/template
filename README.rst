Spring Framework
----------------

The Spring Framework provides a comprehensive programming and
configuration model for modern Java-based enterprise applications -- on
any kind of deployment platform. A key element of Spring is
infrastructural support at the application level: Spring focuses on the
"plumbing" of enterprise applications so that teams can focus on
application-level business logic, without unnecessary ties to specific
deployment environments.

The framework also serves as the foundation for `Spring
Integration <https://github.com/spring-projects/spring-integration>`__,
`Spring Batch <https://github.com/spring-projects/spring-batch>`__ and
the rest of the Spring `family of
projects <http://spring.io/projects>`__. Browse the repositories under
the `Spring organization <https://github.com/spring-projects>`__ on
GitHub for a full list.

Code of Conduct
---------------

This project adheres to the Contributor Covenant `code of
conduct <CODE_OF_CONDUCT.adoc>`__. By participating, you are expected to
uphold this code. Please report unacceptable behavior to
spring-code-of-conduct@pivotal.io.

Downloading Artifacts
---------------------

See `downloading Spring
artifacts <https://github.com/spring-projects/spring-framework/wiki/Downloading-Spring-artifacts>`__
for Maven repository information. Unable to use Maven or other
transitive dependency management tools? See `building a distribution
with
dependencies <https://github.com/spring-projects/spring-framework/wiki/Building-a-distribution-with-dependencies>`__.

Documentation
-------------

See the current
`Javadoc <http://docs.spring.io/spring-framework/docs/current/javadoc-api/>`__
and `reference
docs <http://docs.spring.io/spring-framework/docs/current/spring-framework-reference/>`__.

Getting Support
---------------

Check out the `spring <http://spring.io/questions>`__ tags on `Stack
Overflow <http://stackoverflow.com/faq>`__. `Commercial
support <http://spring.io/services>`__ is available too.

Issue Tracking
--------------

Report issues via the `Spring Framework
JIRA <https://jira.spring.io/browse/SPR>`__. Understand our issue
management process by reading about `the lifecycle of an
issue <https://github.com/spring-projects/spring-framework/wiki/The-Lifecycle-of-an-Issue>`__.
Think you've found a bug? Please consider submitting a reproduction
project via the
`spring-framework-issues <https://github.com/spring-projects/spring-framework-issues#readme>`__
GitHub repository. The
`readme <https://github.com/spring-projects/spring-framework-issues#readme>`__
there provides simple step-by-step instructions.

Building from Source
--------------------

The Spring Framework uses a `Gradle <http://gradle.org>`__-based build
system. In the instructions below,
```./gradlew`` <http://vimeo.com/34436402>`__ is invoked from the root
of the source tree and serves as a cross-platform, self-contained
bootstrap mechanism for the build.

Prerequisites
~~~~~~~~~~~~~

`Git <http://help.github.com/set-up-git-redirect>`__ and `JDK 8 update
20 or later <http://www.oracle.com/technetwork/java/javase/downloads>`__

Be sure that your ``JAVA_HOME`` environment variable points to the
``jdk1.8.0`` folder extracted from the JDK download.

Check out sources
~~~~~~~~~~~~~~~~~

``git clone git@github.com:spring-projects/spring-framework.git``

Import sources into your IDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run ``./import-into-eclipse.sh`` or read ``import-into-idea.md`` as
appropriate. > **Note:** Per the prerequisites above, ensure that you
have JDK 8 configured properly in your IDE.

Install all spring-\* jars into your local Maven cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``./gradlew install``

Compile and test; build all jars, distribution zips, and docs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``./gradlew build``

... and discover more commands with ``./gradlew tasks``. See also the
`Gradle build and release
FAQ <https://github.com/spring-projects/spring-framework/wiki/Gradle-build-and-release-FAQ>`__.

Contributing
------------

`Pull requests <http://help.github.com/send-pull-requests>`__ are
welcome; see the `contributor
guidelines <https://github.com/spring-projects/spring-framework/blob/master/CONTRIBUTING.md>`__
for details.

Staying in Touch
----------------

Follow [@SpringCentral][] as well as [@SpringFramework][] and its `team
members <https://twitter.com/springframework/lists/team/members>`__ on
Twitter. In-depth articles can be found at `The Spring
Blog <http://spring.io/blog/>`__, and releases are announced via our
`news feed <http://spring.io/blog/category/news>`__.

License
-------

The Spring Framework is released under version 2.0 of the `Apache
License <http://www.apache.org/licenses/LICENSE-2.0>`__.

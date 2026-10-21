<?php
/*
 * Plugin Name: Alternate host
 * Description: Lets the site be viewed under a second hostname (e.g. a test
 *   URL) by rewriting the canonical URL stored in the database to the current
 *   one in every page. Active only when wp-config defines WP_CANONICAL_URL and
 *   WP_HOME differs from it; see _infra/websites.busboom.org/compose.yaml.
 */

if ( defined( 'WP_CANONICAL_URL' ) && defined( 'WP_HOME' ) && WP_HOME !== WP_CANONICAL_URL ) {
	ob_start( function ( $html ) {
		$from = array( WP_CANONICAL_URL, str_replace( '/', '\/', WP_CANONICAL_URL ) );
		$to   = array( WP_HOME, str_replace( '/', '\/', WP_HOME ) );
		return str_replace( $from, $to, $html );
	} );
}

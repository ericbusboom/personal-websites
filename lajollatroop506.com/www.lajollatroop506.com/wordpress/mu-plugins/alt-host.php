<?php
/*
 * Plugin Name: Alternate host
 * Description: Rewrites site URLs in every page to the host being viewed.
 *   Old origins left in post content (http://www., the wp.do.cnshost.net
 *   staging host) always become WP_HOME. When wp-config defines
 *   WP_CANONICAL_URL and WP_HOME differs from it (e.g. a test URL), the
 *   canonical URL is rewritten too; see _infra/websites.busboom.org/compose.yaml.
 */

ob_start( function ( $html ) {
	$home = untrailingslashit( home_url() );
	$from = array( 'http://www.lajollatroop506.com', 'http://wp.do.cnshost.net', 'https://wp.do.cnshost.net' );
	if ( defined( 'WP_CANONICAL_URL' ) && WP_HOME !== WP_CANONICAL_URL ) {
		$from[] = WP_CANONICAL_URL;
	}
	$from = array_values( array_diff( $from, array( $home ) ) );
	$to   = array_fill( 0, count( $from ), $home );
	$html = str_replace( $from, $to, $html );
	return str_replace(
		array_map( function ( $u ) { return str_replace( '/', '\/', $u ); }, $from ),
		str_replace( '/', '\/', $home ),
		$html
	);
} );
